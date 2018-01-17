# SQL
Always, when there is a lot of data, we can't read all into the memory, so we use database to get the data.
In order to query data, we need to use SQL language.  
Here, we use SQLite module, then we can use SQL command in Python

- keywords are "SELECT","FROM", "LIMIT", "WHERE"

```
"SELECT column1, column2, ... FROM table1 [LIMIT 5"] [WHERE condition <columnx>]

```
- this means in the labrary, there is a table named "table1", it has many columns.
Now you want to query column1 and column2. And you only want to check the first 5 columns.

```
import sqlite3
# connect with database with a cursor
conn = sqlite3.connect('xxx.db')
cur = conn.cursor()

# SQL command
query = "SELECT column1, column2 FROM table1 LIMIT n"

# run SQL command
cur.execute(query)

# get all query results, if only want to get one use cutr.fetchone()
mycolumn = cur.fetchall()
conn.close()

print(column1)
```
The output looks like [(a1,b1),(a2,b2),...], it is a list, and each element is a tuple.

