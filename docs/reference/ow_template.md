---
layout: default
title: ow.template
parent: Reference
grand_parent: OpenAF docs
---

{% raw %}
## ow.template

[Source: `06414cd9`](https://github.com/OpenAF/openaf/blob/06414cd9204e918daa1e2971ce904783299db333/js/owrap.template.js) · [Baseline](../source-snapshot.md)

### ow.template.addConditionalHelpers

`ow.template.addConditionalHelpers()`

````text
Adds helper functions equivalent to assemble.io comparison helpers starting with "$" See more in http://assemble.io/helpers/helpers-comparison.html
````

### ow.template.addFormatHelpers

`ow.template.addFormatHelpers()`

````text
Adds all functions of ow.format as helpers with the prefix owFormat_.
````

### ow.template.addHelper

`ow.template.addHelper(aHelperName, aFunction)`

````text
Adds aFunction as aHelperName.
````

### ow.template.addHelpers

`ow.template.addHelpers(aPrefix, aObject)`

Registers all `aObject` functions as helpers. These helpers identifier will be composed by `aPrefix` + Name of the each function.

(available after `ow.loadTemplate()`)

### ow.template.addInLineCSS2HTML

`ow.template.addInLineCSS2HTML(aHTML, aCustomCSSMap) : String`

````text
Given aHTML (usually the result of parseMD2HTML) applies a custom inline css (aCustomCSSMap) usually useful to send HTML to  email clients. This custom map should be composed of a html tag entity tag (e.g. "p") and, as value, the css style to apply (e.g. "color: red;"). The map will be applied to all html entities on aHTML. If aCustomCSSMap is not provided a default one (suited for markdown html) will be applied.
````

### ow.template.addOpenAFHelpers

`ow.template.addOpenAFHelpers()`

Adds custom helpers:

- `$debug`: calls sprint for the parameter
- `$stringify`: stringify the parameter
- `$stringifyInLine`: stringify in the same line the parameter
- `$toYAML`: returns the YAML version of the parameter
- `$toKYAML`: returns the KYAML version fo the parameter
- `$toJSON`: returns the JSON version of the parameter
- `$toTOON`: returns the TOON version of the parameter
- `$env`: returns the current environment variable identified by the parameter
- `$escape`: returns an escaped version of the parameter
- `$acolor`: returns an ansi color (first argument) escape sequence of the string parameter (second argument)
- `$f`: uses the `$f` format function
- `$ft`: uses the `$ft` format function
- `$path`: uses the `$path` function to query objects
- `$from`: uses the `$from` & fromNLinq to query objects
- `$oafp`: uses the oafp function to parse the provided JSON/SLON string and return the results
- `$toSLON`: returns the `ow.format.toSLON` version of an object
- `$get`: returns the corresponding value for a key on `$get`
- `$getObj`: equivalent to `$get` with the extra parameter for `$$.get` path
- `$dateDiff`: returns a number of seconds for a provided date optionally (second argument) with minutes, hours, days, months, weeks or years and (third argument) a default value
- `$switch`: equivalent to a javascript switch
- `$case`: to be used with `$switch` for each case
- `$default`: to be used with `$switch` for each case
- `$ptable`: returns an ansi ascii printTable representation of an object
- `$mdtable`: returns a markdown table representation of an array object
- `$ptree`: returns an ansi ascii printTree representation of an object
- `$pchart`: returns an ansi ascii line chart with an object and a format string: "unit path:color:legend... [-min:0] [-max:100] [-hsize:40] [-vsize:10]"
- `$pbar`: returns an ansi ascii progress bar with a value and a max value, a min value, a size, an indicator and space char
- `$pbars`: returns an ansi ascii tree of progress bars with a format string: "unit path:color:legend... [-min:0] [-max:100] [-hsize:40]"
- `$output`: returns an `$output` representation of an object (`aObj` as 1st arg and options in slon as 2nd arg)
- `$cjson`: returns an ansi ascii colority representation fo an object
- `$cslon`: returns an ansi ascii colored SLON representation of an object
- `$pmap`: returns an ansi ascii printMap representation of an object
- `$jsmap`: returns a HTML representation of an object
- `$t`: given a template and an object instance, as arguments, will process and return the template
- `$date`: converts the argument provided to date
- `$isoDate`: converts the argument provided to an ISO date string
- `$number`: casts the argument provided to number
- `$boolean`: casts the argument provided to boolean
- `$string`: casts the argument provided to string
- `$keys`: returns an array of keys of the provided map
- `$values`: returns an array of values of the provided map
- `$__`: returns a undefined value
- `$alen`: returns the ansi length of the argument provided
- `$len`: returns the string length of the argument provided
- `$repeat`: shortcut to the OpenAF's repeat function
- `$range`: shortcut to the OpenAF's range function
- `$a2m`: shortcut to the OpenAF's `$a2m` function
- `$a4m`: shortcut to the OpenAF's `$a4m` function
- `$m2a`: shortcut to the OpenAF's `$m2a` function
- `$m4a`: shortcut to the OpenAF's `$m4a` function
- `$nvl`: shortcut to the OpenAF's nvl function
- `$pass`: returns an empty string
- `$p`: returns the provided literal
- `$sline`: shortcut to the OpenAF's format withSideLine
- `$set`: block set of a provided key
- `$concat`: concatenates all arguments as a single value
- `$nl`: returns a new line character

### ow.template.addPartial

`ow.template.addPartial(aPartialName, aSource)`

````text
Registers aSource template as a reusable aPartialName in other templates.
````

### ow.template.compile

`ow.template.compile(aSource, anOptionsMap) : String`

````text
Tries to precompile aSource and returns a String that can be used with ow.template.execCompiled. Optionally you can provide anOptionsMap for the Handlebars precompiler (see more on ow.template.saveCompiledHBS).
````

### ow.template.delHelper

`ow.template.delHelper(aHelperName)`

````text
Unregister aHelperName that had been previously added with ow.template.addHelper.
````

### ow.template.delPartial

`ow.template.delPartial(aPartialName)`

````text
Unregisters aPartialName that had been previously added with ow.template.addPartial
````

### ow.template.execCompiled

`ow.template.execCompiled(aCompiledObject) : Function`

````text
Tries to execute a previously precompiled Handlebars template (for example, using ow.template.compile) and return it as a Handlebars template functions.
````

### ow.template.getTemplate

`ow.template.getTemplate(aSource) : Function`

````text
Returns a template function, given aSource, that accepts an object as argument and returns the correspoding template filled with the values provided.
````

### ow.template.html.genStaticVersion

`ow.template.html.genStaticVersion(anOriginalHTML) : String`

````text
Tries to convert anOriginalHTML with "src" based tags like img, script & stylesheet link tags into a single HTML embeeding  all content.
````

### ow.template.html.genStaticVersion4MD

`ow.template.html.genStaticVersion4MD(anOriginalMD) : String`

````text
Tries to convert a markdown into a single HTML embeeding css and image contents.
````

### ow.template.html.genStaticVersion4MDFile

`ow.template.html.genStaticVersion4MDFile(anOriginalMDFile) : String`

````text
Tries to convert a markdown file into a single HTML embeeding css and image contents.
````

### ow.template.html.inlineImageTag

`ow.template.html.inlineImageTag(aImageFile, justPartial) : String`

````text
Returns a base64 representation of aImageFile to include in markdown/html content. If justPartial = true then only the src  part of the html img tag is returned.
````

### ow.template.html.inlineSrc

`ow.template.html.inlineSrc(aFile, aPrefix, aSuffix) : String`

````text
Returns a base64 representation of aFile to include in markdown/html content. If aPrefix and/or aSuffix is provided it will be prefixed and suffixed to the output.
````

### ow.template.html.inlineSrcURL

`ow.template.html.inlineSrcURL(aURL, aPrefix, aSuffix) : String`

````text
Returns a base64 representation of aURL to include in markdown/html content. If aPrefix and/or aSuffix is provided it will be prefixed and suffixed to the output.
````

### ow.template.html.njsmapAutoTheme

`ow.template.html.njsmapAutoTheme() : String`

````text
Returns a script to automatically set the njsmap theme based on the user's preference if the MD_DARKMODE flag is set to "auto".
````

### ow.template.html.parseMap

`ow.template.html.parseMap(aMapOrArray, genParts, forceDark) : Object`

````text
Returns a string with a HTML representation of the aMapOrArray provided or, if genParts = true, a map with the style css and the out string necessary. If forceDark = true it will force the dark mode.
````

### ow.template.html.parseMapInHTML

`ow.template.html.parseMapInHTML(aMapOrArray, forceDark) : String`

````text
Returns a full HTML page with the nJSMap representation of the aMapOrArray provided. If forceDark = true it will force the dark mode.
````

### ow.template.html.thinFontCSS

`ow.template.html.thinFontCSS(aSize) : String`

````text
Returns a CSS string for a thin font with the provided aSize (in points).
````

### ow.template.html.thinFontDiv

`ow.template.html.thinFontDiv(aTxt, aSize, aExtra) : String`

````text
Returns a HTML div part to write aTxt with the provided aSize (in points). Optionally aExtra css can be added.
````

### ow.template.html.thinFontSpan

`ow.template.html.thinFontSpan(aTxt, aSize, aExtra) : String`

````text
Returns a HTML span part to write aTxt with the provided aSize (in points). Optionally aExtra css can be added.
````

### ow.template.loadCompiledHBS

`ow.template.loadCompiledHBS(aFilename) : Function`

````text
Tries to load a previously precompiled Handlebars template (for example, using ow.template.saveCompiledHBS) and return it as a Handlebars template functions.
````

### ow.template.loadHBSs

`ow.template.loadHBSs(aMapOfHBSs) : Function`

````text
Given a map where the key is a hbs template key and the value is the filepath of a HBS file, will pre-compile the HBS files and return a function(key, data). This function can be used to execute a the pre-compiled templates using the hbs template key and passing the corresponding data map to be used on that template returning the template parsed. Note: the filepath can indicate a file inside a zip file like 'some/path/a.zip::file'.
````

### ow.template.loadPartialHBS

`ow.template.loadPartialHBS(aMapOfParialHBSs)`

````text
Given a map where the key is a partial hbs template key and the value is the filepath of a HBS file, will load it and add it as a template partial. Note: the filepath can indicate a file inside a zip file like 'some/path/a.zip::file'.
````

### ow.template.md.fromTable

`ow.template.md.fromTable(aMarkdown) : Array`

````text
Tries to transform aMarkdown table text into an array.
````

### ow.template.md.htmlArrayMap

`ow.template.md.htmlArrayMap(anMapOrArray) : String`

````text
Converts anMapOrArray into a div html suitable to be added to a markdown.
````

### ow.template.md.maxWidth

`ow.template.md.maxWidth(aValue) : String`

````text
Generates the appropriate HTML to set the MD page width to aValue (e.g. 800px). If aValue not defined it will unset the default limit.
````

### ow.template.md.table

`ow.template.md.table(anArray) : String`

````text
Converts anArray into a markdown table string.
````

### ow.template.parse

`ow.template.parse(aSource, someData) : String`

````text
Returns the results of using someData to the template defined on the aSource provided. Note: for parallel processing you should use ow.template.compile since Handlebars might not be thread-safe.
````

### ow.template.parseHBS

`ow.template.parseHBS(aFilename, someData) : String`

````text
Returns the results of using someData with the template defined on aFilename (tip: use the extension hbs).
````

### ow.template.parseMD2HTML

`ow.template.parseMD2HTML(aMarkdownString, isFull, removeMaxWidth, extraDownOptions, forceDark) : String`

Given `aMarkdownString` will parse it with showdown (using the github flavor) and return the HTML in a string. If `isFull` = true
it will produce a complete HTML with references for the highlight library+css and github markdown css included internally in OpenAF.
If `removeMaxWidth` = true it will remove the max-width css style. You can provide `extraDownOptions` to be used with showdown and
`forceDark` to force the dark mode.
Example:

```javascript
ow.server.httpd.route(hs, ow.server.httpd.mapRoutesWithLibs(hs, {
   "/md": (req) => { return hs.replyOKHTML(ow.template.parseMD2HTML(io.readFileString("README.md"), true)) }
}), (req) => { return hs.replyOKText("nothing here...");})
```

### ow.template.saveCompiledHBS

`ow.template.saveCompiledHBS(aFilename, aSource, anOptionsMap)`

Tries to precompile `aSource` and save the result into `aFilename` (tip: use the extension hbsc).
This can later be loaded again using `ow.template.loadCompiledHBS`, for example.
Optionally you can provide `anOptionsMap` for the Handlebars precompiler (see more on the options for Handlebars.precompile).
Example:

```javascript
var source = "My name is {{myname}}. I'm a\n{{#each role}}\t- {{this}}\n{{/each}}";
ow.template.saveCompiledHBS("myroles.hbsc", source, {
   "knownHelpers": { each: true }, "knownHelpersOnly": true
});
```

### ow.template.saveHBS

`ow.template.saveHBS(aFilename, aSource)`

````text
Saves aSource Handlebars template into aFilename (tip: use the extension hbs).
````

### ow.template.unloadPartialHBSs

`ow.template.unloadPartialHBSs(aMapOFPartialHBSs)`

````text
Given the same map provided to ow.template.loadPartialHBS will actually unload them as template partials.
````

### parseHTML2MD

`parseHTML2MD(aHTMLString, includeScripts) : String`

````text
Given an HTML string and a flag indicating whether to include scripts, this function converts the HTML to Markdown.
````
{% endraw %}
