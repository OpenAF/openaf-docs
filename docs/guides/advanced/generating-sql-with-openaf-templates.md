---
layout: default
title: Generating SQL with OpenAF templates
parent: Advanced
grand_parent: Guides
---

# Generating SQL with OpenAF templates

Since OpenAF is Java and Javascript it can take advantage of the two languages. The javascript [Handlebars](http://handlebarsjs.com/) library comes already bundled in OpenAF and provides the ability to create any kind of text templates which can be reused and changed without any code changes to a script.

## Simple example

To show this let's take the hypothetical example of creating several reference tables (for the sake of space on the article we are going to consider that the fields are fixed). Handlebars will render any template using a javascript object. So let's create one for our example:

`tables.json`
````javascript
{
  "appUser": "PROJ_APP",
  "datUser": "PROJ_DAT",
  "tablespace": "PROJ_TAB",
  "tables": [
    {
      "tableName": "tab_1"
    },
    {
      "tableName": "tab_2"
    },
    {
      "tableName": "TAB_3"
    }
  ]
}
````

So we are specifying the application (app) and data (dat) users to use, the tablespace to use and the table names. Now let's create a Handlebars template file (hbs):

{% raw %}`table_creation.hbs`
````sql
-- Creating tables
--

{{#each TABLES}}
-- Table for {{../datUser}}.{{tableName}}
CREATE TABLE {{../datUser}}.{{tableName}} (col1 NUMBER(8), col2 VARCHAR(500)) TABLESPACE {{../tablespace}}
{{/each}}
````{% endraw %}

Looking at the JSON object this template is iterating on the tables array, getting the tableName. datUser and tablespace are gather from the parent to the tables array.

And let's create the OpenAF script to bundle everything:

````javascript
ow.loadTemplate();
print(ow.template.parseHBS("table_creation.hbs", io.readFile("tables.json"));
````

And that's it, when you run it you will get this:

````sql
-- Creating tables
--
 
-- Table for PROJ_DAT.tab_1
CREATE TABLE PROJ_DAT.tab_1 (col1 NUMBER(8), col2 VARCHAR(500)) TABLESPACE PROJ_TAB
-- Table for PROJ_DAT.tab_2
CREATE TABLE PROJ_DAT.tab_2 (col1 NUMBER(8), col2 VARCHAR(500)) TABLESPACE PROJ_TAB
-- Table for PROJ_DAT.TAB_3
CREATE TABLE PROJ_DAT.TAB_3 (col1 NUMBER(8), col2 VARCHAR(500)) TABLESPACE PROJ_TAB
````

But if we are creating tables in a data schema for which we want to create synonyms on the application schema. Well, now we just need to change the template for that:

{% raw %}`table_creation.hbs`
````sql
-- Creating synonyms
--

{{#each TABLES}}
-- Synonym for {{../appUser}}.{{tableName}}
CREATE OR REPLACE SYNONYM {{../appUser}}.{{tableName}} FOR {{../datUser}}.{{tableName}};
GRANT ALL ON {{tableName}} TO {{../appUser}} WITH GRANT OPTION;
{{/each}}

-- Creating tables
--

{{#each TABLES}}
-- Table for {{../datUser}}.{{tableName}}
CREATE TABLE {{../datUser}}.{{tableName}} (col1 NUMBER(8), col2 VARCHAR(500)) TABLESPACE {{../tablespace}}
{{/each}}
````{% endraw %}

And execute the unchanged OpenAF script:

````sql
-- Creating synonyms
--
 
-- Synonym for PROJ_APP.tab_1
CREATE OR REPLACE SYNONYM PROJ_APP.tab_1 FOR PROJ_DAT.tab_1;
GRANT ALL ON tab_1 TO PROJ_APP WITH GRANT OPTION;
-- Synonym for PROJ_APP.tab_2
CREATE OR REPLACE SYNONYM PROJ_APP.tab_2 FOR PROJ_DAT.tab_2;
GRANT ALL ON tab_2 TO PROJ_APP WITH GRANT OPTION;
-- Synonym for PROJ_APP.TAB_3
CREATE OR REPLACE SYNONYM PROJ_APP.TAB_3 FOR PROJ_DAT.TAB_3;
GRANT ALL ON TAB_3 TO PROJ_APP WITH GRANT OPTION;
 
-- Creating tables
--
 
-- Table for PROJ_DAT.tab_1
CREATE TABLE PROJ_DAT.tab_1 (col1 NUMBER(8), col2 VARCHAR(500)) TABLESPACE PROJ_TAB
-- Table for PROJ_DAT.tab_2
CREATE TABLE PROJ_DAT.tab_2 (col1 NUMBER(8), col2 VARCHAR(500)) TABLESPACE PROJ_TAB
-- Table for PROJ_DAT.TAB_3
CREATE TABLE PROJ_DAT.TAB_3 (col1 NUMBER(8), col2 VARCHAR(500)) TABLESPACE PROJ_TAB
````

## Using helpers

We could stop the example but if you notice some table names are not all upper cases. And we like our generated SQL to be pretty :) To do that we just make some slights changes to the OpenAF script to include a helper function:

````javascript
ow.loadTemplate();
ow.template.addHelper("upper", function(aString) { return aString.toUpperCase();})
print(ow.template.parseHBS("table_creation.hbs", io.readFile("tables.json"));
````

and use the function inside the template:

{% raw %}`table_creation.hbs`
````sql
-- Creating tables
--

{{#each TABLES}}
-- Table for {{../datUser}}.{{upper tableName}}
CREATE TABLE {{../datUser}}.{{UPPER tableName}} (col1 NUMBER(8), col2 VARCHAR(500)) TABLESPACE {{../tablespace}}
{{/each}}
````{% endraw %}

The result:

````sql
-- Creating tables
--
 
-- Table for PROJ_DAT.TAB_1
CREATE TABLE PROJ_DAT.TAB_1 (col1 NUMBER(8), col2 VARCHAR(500)) TABLESPACE PROJ_TAB
-- Table for PROJ_DAT.TAB_2
CREATE TABLE PROJ_DAT.TAB_2 (col1 NUMBER(8), col2 VARCHAR(500)) TABLESPACE PROJ_TAB
-- Table for PROJ_DAT.TAB_3
CREATE TABLE PROJ_DAT.TAB_3 (col1 NUMBER(8), col2 VARCHAR(500)) TABLESPACE PROJ_TAB
````

## Using conditions

Well, not all the tables will be equally created. We might not want Oracle logging for some. Let's note that on the json data:

`tables.json`
````javascript
{
  "appUser": "PROJ_APP",
  "datUser": "PROJ_DAT",
  "tablespace": "PROJ_TAB",
  "tables": [
    {
      "tableName": "tab_1"
    },
    {
      "tableName": "tab_2",
      "nologging": true
    },
    {
      "tableName": "TAB_3"
    }
  ]
}
````

And change the template:

{% raw %}`table_creation.hbs`
````sql
-- Creating tables
--

{{#each TABLES}}
-- Table for {{../datUser}}.{{tableName}}
CREATE TABLE {{../datUser}}.{{tableName}} (col1 NUMBER(8), col2 VARCHAR(500)) {{#if nologging}}NOLOGGING{{/IF}} TABLESPACE {{../tablespace}}
{{/each}}
````{% endraw %}

Executing the unchanged script:

````sql
-- Creating tables
--
 
-- Table for PROJ_DAT.tab_1
CREATE TABLE PROJ_DAT.tab_1 (col1 NUMBER(8), col2 VARCHAR(500))  TABLESPACE PROJ_TAB
-- Table for PROJ_DAT.tab_2
CREATE TABLE PROJ_DAT.tab_2 (col1 NUMBER(8), col2 VARCHAR(500)) NOLOGGING TABLESPACE PROJ_TAB
-- Table for PROJ_DAT.TAB_3
CREATE TABLE PROJ_DAT.TAB_3 (col1 NUMBER(8), col2 VARCHAR(500))  TABLESPACE PROJ_TAB
````

## Using template parts for increase reusability

Well this way we are going to end with lots of hbs files and little reusability besides copy+paste. Can we solve that? Yes, we case use partials. So let's create two sub templates for synonyms and tables:

{% raw %}`table_creation.hbs`
````sql
-- Creating tables for {{for}}
--

{{#each TABLES}}
-- Table for {{../datUser}}.{{upper tableName}}
{{#if NUMBER}}
CREATE TABLE {{../datUser}}.{{UPPER tableName}} (col1 NUMBER(8), col2 NUMBER(25)) TABLESPACE {{../tablespace}}
{{ELSE}}
CREATE TABLE {{../datUser}}.{{UPPER tableName}} (col1 NUMBER(8), col2 VARCHAR(500)) TABLESPACE {{../tablespace}}
{{/IF}}
{{/each}}
````{% endraw %}

Now one for the synonyms:

{% raw %}`syn_creation.hbs`
````sql
-- Creating synonyms for {{for}}
--

{{#each TABLES}}
-- Synonym for {{../appUser}}.{{upper tableName}}
CREATE OR REPLACE SYNONYM {{../appUser}}.{{UPPER tableName}} FOR {{../datUser}}.{{UPPER tableName}};
GRANT ALL ON {{UPPER tableName}} TO {{../appUser}} WITH GRANT OPTION;
{{/each}}
````{% endraw %}

And a main template to refer to these two sub templates (partials):

{% raw %}`sql_creation.hbs`
````sql
{{> synonyms FOR="ref tables"}}
{{> TABLES   FOR="ref tables"}}
````{% endraw %}

Now we just need to alter the OpenAF script to register the sub templates (partials):

````javascript
ow.loadTemplate();
ow.template.addHelper("upper", function(aString) { return aString.toUpperCase();})
ow.template.addPartial("tables", io.readFileString("table_creation.hbs"));
ow.template.addPartial("synonyms", io.readFileString("syn_creation.hbs"));
print(ow.template.parseHBS("sql_creation.hbs", io.readFile("tables.json"));
````

And we are done. We now can improve the synonyms and table creation separately and reuse those for different proposes while keep the reference to the same template file.

## What if we want to generate something else? Is this only for SQL?

Well, it's text based. Originally Handlebars is used for web templating parsing templates using javascript. So just change the template:

{% raw %}````
SQL generation report
---------------------

Using the schemas:
- DAT = {{datUser}}
- APP = {{appUser}}

and the tablespace {{tablespace}}, the following reference Oracle objects DDL were generated:

{{#each tables}}
- The {{#if number}}number {{/if}}reference table {{upper tableName}} for the schema {{../datUser}} and tablespace {{../tablespace}}.
- The synonym from {{../datUser}}'s {{upper tableName}} for {{../appUser}}.
{{/each}}
````{% endraw %}

and it's done:

````
SQL generation report
---------------------

Using the schemas:
- DAT = PROJ_DAT
- APP = PROJ_APP

And tablespaces:
- LARGE = PROJ_TAB

The following reference Oracle objects DDL were generated:

- The reference table TAB_1 for the schema PROJ_DAT and tablespace PROJ_TAB.
- The synonym from PROJ_DAT's TAB_1 for PROJ_APP.
- The reference table TAB_2 for the schema PROJ_DAT and tablespace PROJ_TAB.
- The synonym from PROJ_DAT's TAB_2 for PROJ_APP.
- The reference table TAB_3 for the schema PROJ_DAT and tablespace PROJ_TAB.
- The synonym from PROJ_DAT's TAB_3 for PROJ_APP.
````

## Where can I learn more about Handlebars?

There is more functionality available including pre-compiling templates for performance (_ow.template.compile_, _ow.template.execCompiled_, _ow.template.loadCompiledHBS_ and _ow.template.saveCompiledHBS_). There are several examples through the internet. But you can start with:

  * Expressions (escaping, whitespace control, helpers, &#46;&#46;&#46;): http://handlebarsjs.com/expressions.html
  * Partials (dynamic partials, block partials, inline partials): http://handlebarsjs.com/partials.html
  * Built-in helpers (if, unless, each, with, lookup, log, &#46;&#46;&#46;): http://handlebarsjs.com/builtin_helpers.html
  * Block helpers: http://handlebarsjs.com/block_helpers.html