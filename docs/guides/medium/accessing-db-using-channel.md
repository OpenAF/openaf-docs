---
layout: default
title: Accessing a database using an OpenAF channel
parent: Medium
grand_parent: Guides
---

# Accessing a database using an OpenAF channel

> OpenAF version >= 20250315

When using the [OpenAF channel](../../concepts/OpenAF-Channels.md) functionality it's possible to wrap it's functionality around a database table. Any JDBC driver accessible database where standard SQL is valid can be used.

> Check also on how to [use different JDBC drivers](../../guides/ojobio/db-drivers.md) in OpenAF

Let's use a simple example with a H2 file database.

## Creating the example database

For this example we will create a dummy _employees_ table in a local H2 file.

### Creating the table using oafp:

Execute:

```sql
cat <<_EOF | oafp in=db indbjdbc="jdbc:h2:./data" indbuser=sa indbpass=sa indbexec=true
CREATE TABLE employees (
    id             INT             PRIMARY KEY,
    first_name     VARCHAR(50)     NOT NULL,
    last_name      VARCHAR(50)     NOT NULL,
    email          VARCHAR(100)    UNIQUE NOT NULL,
    hire_date      DATE            NOT NULL DEFAULT CURRENT_DATE,
    salary         DECIMAL(10,2)   NOT NULL CHECK (salary >= 0),
    department_id  INT,
    active         BOOLEAN         NOT NULL DEFAULT TRUE
);
_EOF
```

### Filling up sample data using oafp:

Execute:

```sql
cat <<_EOF | oafp in=db indbjdbc="jdbc:h2:./data" indbuser=sa indbpass=sa indbexec=true
INSERT INTO employees
    (id, first_name, last_name, email, hire_date, salary, department_id, active)
VALUES
    (1,  'John',    'Doe',     'john.doe@example.com',      '2020-01-15', 60000.00, 1, TRUE),
    (2,  'Jane',    'Smith',   'jane.smith@example.com',    '2019-06-01', 75000.00, 2, TRUE),
    (3,  'Bob',     'Johnson', 'bob.johnson@example.com',   '2021-03-20', 55000.00, 1, FALSE),
    (4,  'Alice',   'Brown',   'alice.brown@example.com',   '2022-11-30', 85000.00, 3, TRUE),
    (5,  'Michael', 'Davis',   'michael.davis@example.com', '2018-08-07', 95000.00, 2, TRUE);
_EOF
```

### Checking the inserted data:

Execute:

```sql
oafp data="select * from employees" in=db indbjdbc="jdbc:h2:./data" indbuser=sa indbpass=sa out=ctable
```

## OpenAF DB channel type

With a sample database table created lets know setup and use an OpenAF DB channel.

When creating an OpenAF DB channel you have the following options available:

| Option | Mandatory? | Type | Description |
|--------|------------|------|-------------|
| **db** | Yes | DB object | The database object to access the database table. |
| **from** | Yes | String | The name of the database table or object (don't use double quotes). |
| **keys** | No | Array | An array of fields keys to use (don't use double quotes). |
| **cs** | No | Boolean | Determines if the database is case sensitive for table and field names (defaults to false). |

For this example you can use these options like this:

```javascript
// Creating the database object
var db = new DB("jdbc:h2:./data", "sa", "sa")

// Creating the OpenAF DB channel
$ch("employees").create("db", { db: db, from: "employees", keys: ['id'], cs: false })
```

### Accessing the database data

With the _employees_ OpenAF channel created you can now access the database data using the channel's methods. For example:

```javascript
// Retrieve a single record
cprint( $ch("employees").get({ id: 3 }) )

// Retrieve a list of all key values
cprint( $ch("employees").getKeys() )
```

### Modifying the database data

You can also use the channel's methods to modify the database data. For example:

```javascript
// Creating a new record
$ch("employees").set({ id: 6 }, { id: 6, first_name: 'Emma', last_name: 'Wilson', email: 'emma.wilson@example.com', hire_date: '2023-05-10', salary: '72000.00', department_id: 2, active: true })

// Checking the newly created record
cprint( $ch("employees").get({ id: 6 }) )
```

> Keep in mind that the field names are case-sensitive. The SQL statements that OpenAF generates should reflect the casing of the field names valid for the corresponding database.

Let's delete a record:

```javascript
// Check the size previously
cprint( $ch("employees").size() )

// Deleting the record
$ch("employees").unset({ id: 6 })

// Check the size aftewards
cprint( $ch("employees").size() )
```

### Destroying the channel and closing the database

Don't forget, on the end of your code, to destroy the channel and close the database connection:

```javascript
$ch("employees").destroy()
db.close()
```

> Despite the _destroy_ name nothing will happen to the database data once an OpenAF channel is destroyed. The channel simply releases its resources.