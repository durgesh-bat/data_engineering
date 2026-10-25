# Python + PostgreSQL — Lessons 1 and 2

**Learning track:** Data Engineering Foundations  
**Environment:** Debian Linux, Python virtual environment, PostgreSQL, Psycopg 3  
**Project root:** `~/Desktop/Data_Engineering`

These notes recap the first two lessons: connecting Python to PostgreSQL, then executing a `SELECT` query and reading its rows.

## Lesson 1 — Connect Python to PostgreSQL

### 1. What each component does

- **PostgreSQL** stores and queries the data.
- **Python** runs the application logic.
- **Psycopg 3** is the Python driver that lets Python communicate with PostgreSQL.
- A **connection** (`conn`) represents a database session.
- A **cursor** (`cur`) executes SQL through that connection and reads query results.

```text
Python program
    |
    v
Psycopg 3 driver
    |
    v
PostgreSQL database
    |
    v
Tables and query results
```

### 2. Activate the project environment

```bash
cd ~/Desktop/Data_Engineering
source .venv/bin/activate
```

If the project is being set up on a new machine, install dependencies first:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

### 3. Connection settings

The project reads local connection settings from `.env` (which must not be committed to Git):

```dotenv
DB_HOST=localhost
DB_PORT=5432
DB_NAME=data_engineering
DB_USER=de_user
DB_PASSWORD=YOUR_LOCAL_PASSWORD
```

The corresponding code uses `python-dotenv` to load the file and passes the values to Psycopg. Do not hardcode real passwords in source code or push them to GitHub.

### 4. Test the connection

File: `Foundations/ETL/db_connect.py`

```python
import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")

settings = {
    "host": os.environ["DB_HOST"],
    "port": int(os.environ["DB_PORT"]),
    "dbname": os.environ["DB_NAME"],
    "user": os.environ["DB_USER"],
    "password": os.environ["DB_PASSWORD"],
}

with psycopg.connect(**settings) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT version();")
        row = cur.fetchone()
        print("PostgreSQL connection successful!")
        print(row[0])
```

Run it from the project root:

```bash
python Foundations/ETL/db_connect.py
```

`PROJECT_ROOT = Path(__file__).resolve().parents[2]` works here because the file lives in `Foundations/ETL/`.

## Lesson 2 — Cursor, `execute()`, and reading rows

### 1. Execute a query

File: `Foundations/ETL/read_students.py`

```python
import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")

settings = {
    "host": os.environ["DB_HOST"],
    "port": int(os.environ["DB_PORT"]),
    "dbname": os.environ["DB_NAME"],
    "user": os.environ["DB_USER"],
    "password": os.environ["DB_PASSWORD"],
}

with psycopg.connect(**settings) as conn:
    with conn.cursor() as cur:
        cur.execute("""
            SELECT id, name, marks
            FROM student
            ORDER BY id;
        """)

        rows = cur.fetchall()

        for row in rows:
            print(row)
```

Run:

```bash
python Foundations/ETL/read_students.py
```

The exact rows depend on the records present in your local `student` table.

### 2. Understand the lines

- `psycopg.connect(**settings)` opens a database connection using the settings dictionary.
- `conn.cursor()` creates a cursor.
- `cur.execute(sql)` sends SQL to PostgreSQL for execution.
- `cur.fetchall()` returns all **remaining** result rows as a Python list.
- Each row is usually returned as a tuple, for example `(102, 'RAHUL', 100)`.
- `ORDER BY id` makes the ordering explicit; without `ORDER BY`, row order is not guaranteed.

### 3. Filter records with `WHERE`

To return students with marks of at least 80, change the query to:

```sql
SELECT id, name, marks
FROM student
WHERE marks >= 80
ORDER BY id;
```

`WHERE` filters rows in PostgreSQL before the result is fetched by Python.

## Important cursor methods — preview

| Method | What it returns |
|---|---|
| `execute(sql, params)` | Executes a SQL statement; it does not itself return all result rows. |
| `fetchone()` | One next row, or `None` when no rows remain. |
| `fetchmany(size=n)` | Up to `n` next rows as a list. |
| `fetchall()` | All remaining rows as a list. |

Rows are consumed as you fetch them. If you call `fetchone()` twice, then `fetchall()`, the latter returns only the rows still remaining after those two fetches.

## Quick practice

1. Run `db_connect.py` and confirm the connection works.
2. Run `read_students.py` and inspect the row tuples.
3. Add `WHERE marks >= 80` and run it again.
4. Explain in your own words the difference between `conn`, `cur`, `execute()`, and `fetchall()`.

## Common issues

- **Wrong file path:** From the project root use `python Foundations/ETL/db_connect.py`. If already inside `Foundations/ETL/`, use `python db_connect.py`.
- **Missing environment variable:** Ensure `.env` exists at `~/Desktop/Data_Engineering/.env` and the keys match the code.
- **Connection refused:** Verify PostgreSQL is running and `DB_HOST`/`DB_PORT` are correct.
- **Table does not exist:** Make sure the code connects to the intended database and that the schema has been created there.
- **Case-sensitive name search:** `WHERE name = %s` is case-sensitive in PostgreSQL text comparisons; `ILIKE` can be used for case-insensitive matching.

## Next lesson

Practice `fetchone()`, `fetchall()`, and `fetchmany()` with the same query, and understand how each call advances through the cursor's result rows.
