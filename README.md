## This is a code challenge for students at TwentyThree
- Author: Mário Gažo
- Date: 2021, September
<hr>

## How to use?
- Part 1:

CLI tool is written as Python script

Usage: <br>
```
py twentythree.py method [id] [--type \<photo|video\>] [--title \<title\>] [--label \<label\>] [--url \<valid url\>]
```

To execute tests, run given command in the root directory:
```
python -m pytest
```

- Part 2

Microservice is written using PHP and SQL

You need to run apache and MySQL server, run `db.sql` to create assets table and one example row. PHP script connects to
localhost DB at port `3306`, it handles requests by detecting request method, checking its parameters and executing SQL 
query. I also rewrite ID from path parameter to query one, although the user doesn't notice, it is done by RewriteRule
in `.htaccess` file.

