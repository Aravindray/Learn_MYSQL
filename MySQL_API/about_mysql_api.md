## How to add library file location In Windows

In windows search find - **Edit the system environment variables** and click *Environment Variables* under *System variables* click *new* if `PYTHONPATH` not exists, Then enter the variable name as `PYTHONPATH` and variable values *the actual file location*. if more than one location user **;** (semicolon) as delimiter.



Alternatively, We can inform the program to search the library file to explicit define them in the script with

``` python
import sys
sys.path.append('D:\\desire\\folder\\location') # Don't forget to user escape char \\
```
