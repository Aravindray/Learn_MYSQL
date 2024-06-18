## How to add library file location In Windows

In windows search find - **Edit the system environment variables** and click *Environment Variables* under *System variables* click *new* if `PYTHONPATH` not exists, Then enter the variable name as `PYTHONPATH` and variable values *the actual file location*. if more than one location user **;** (semicolon) as delimiter.

![Setup PYTHONPATH](https://github.com/Aravindray/Learn_MYSQL/blob/main/assets/setting%20PYTHONPATH%20environment%20variables.png)

Alternatively, We can inform the program to search the library file to explicit define them in the script with

``` python
import sys
sys.path.append('D:\\desire\\folder\\location') # Don't forget to user escape char \\
```

## Handling Special Characters in identifier

In a sql statement the identifier may have special character for example,

```sql
CREATE TABLE some table (i INT);
```

above statement through an error to handle it user **`** (backtick) as quotation to identifier.

```sql
CREATE TABLE `some table` (i INT);

-- Another example., If quoting character appears in identifier just double it abc`def -> `abc``def `
```

cookbook, profile is identifier, but in the below statement it is used as data value. So quote it as data value.

```sql
SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'cookbook' AND TABLE_NAME = 'profile';
```
