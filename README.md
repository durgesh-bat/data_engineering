# Data Engineering Learning Repository

A practical learning repo for Python, SQL, PostgreSQL, ETL, logging, indexes, and Python/PostgreSQL integration. The code here is a cleaned-up, reproducible snapshot reconstructed from our learning work and troubleshooting; it is not a byte-for-byte copy of files from a local PC.

## Current progress

- Python foundations, functions, collections, exceptions, and file handling
- CSV and JSON processing
- REST API extraction with timeouts, retries, pagination, and logging
- ETL: extract, transform, validate, and load
- PostgreSQL basics: filtering, ordering, aggregation, grouping, NULL, joins, transactions, and constraints
- Indexes: primary-key and regular indexes, `EXPLAIN`, `EXPLAIN ANALYZE`, bitmap scans, and composite indexes
- Python/PostgreSQL with Psycopg 3: parameterized SQL, `fetchone()`, `fetchall()`, `executemany()`, UPSERT, and transaction contexts

## Repository layout

```text
data_engineering/
├── README.md
├── requirements.txt
├── .env.example
├── sql/
│   ├── 01_schema.sql
│   └── 02_index_lab.sql
└── Foundations/
    ├── SQL_PROGRESS.md
    └── ETL/
        ├── logger_config.py
        ├── extract.py
        ├── transform.py
        ├── load.py
        ├── main.py
        ├── db_connect.py
        ├── search_student.py
        └── insert_many_students.py
```

## 1. Clone the repository

```bash
git clone https://github.com/durgesh-bat/data_engineering.git
cd data_engineering
```

## 2. Create a virtual environment

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

### Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` and enter your local PostgreSQL credentials. **Never commit `.env` or a real password.** The repository ignores it.

## 3. Create the PostgreSQL database and user

Open psql as a PostgreSQL administrator:

```bash
# Linux
sudo -u postgres psql
```

On Windows, open SQL Shell (psql) or run psql from a terminal with your PostgreSQL administrator account. Then run:

```sql
CREATE ROLE de_user WITH LOGIN PASSWORD 'REPLACE_WITH_A_STRONG_LOCAL_PASSWORD';
CREATE DATABASE data_engineering OWNER de_user;
\q
```

If the database or role already exists, do not run the corresponding CREATE command again. Use the existing credentials and update `.env`.

Load the schema:

```bash
psql -h localhost -U de_user -d data_engineering -f sql/01_schema.sql
```

Enter the password when prompted. Alternatively, connect in psql and run `\i sql/01_schema.sql`.

The schema script creates `course`, `student`, and `api_posts`, with example student/course data. It is intended for a fresh learning database; review it before applying it to a database that already has tables or data.

## 4. Test the Python database connection

```bash
python Foundations/ETL/db_connect.py
```

## 5. Run the ETL pipeline

The pipeline calls the JSONPlaceholder `/posts` API, retries failed requests, paginates through results, validates/transforms records, and UPSERTs them into PostgreSQL.

```bash
python Foundations/ETL/main.py
```

Verify in psql:

```sql
SELECT COUNT(*) FROM api_posts;
SELECT id, user_id, title FROM api_posts ORDER BY id LIMIT 5;
```

JSONPlaceholder commonly returns 100 posts. The loader uses `ON CONFLICT (id) DO UPDATE`, so running the same pipeline again should not create duplicate IDs; existing rows are refreshed.

## 6. Try the student integration examples

```bash
python Foundations/ETL/search_student.py
python Foundations/ETL/insert_many_students.py
```

The insert example uses `ON CONFLICT (id) DO NOTHING`, so it can be run again without creating duplicate rows. It returns no claim that an existing conflicting row was updated.

## 7. Index lab

The large index experiment is separate so it does not run automatically. Review and execute the SQL in `sql/02_index_lab.sql` in your practice database. It creates 1,000,000-row demo tables and uses disk space. You can compare plans with `EXPLAIN` and `EXPLAIN ANALYZE`.

Key lesson: a primary key automatically has an index in PostgreSQL; a foreign key does not automatically create an index on the referencing column. The query planner chooses whether to use an available index.

## Notes

- SQL parameters use Psycopg's `%s` placeholders; do not build SQL by concatenating untrusted input.
- Psycopg connection context managers commit on successful exit and roll back if an exception escapes the context.
- `fetchone()` returns one row (or `None`); `fetchall()` returns all remaining rows.
- `executemany()` executes a statement for multiple parameter sets. For very large loads, PostgreSQL `COPY` is a later topic.
- Logs are written to `Data/etl.log`; the local `Data/` output directory is ignored by Git.

## Current next learning steps

1. Transaction rollback and error propagation
2. `executemany()` vs PostgreSQL `COPY`
3. Advanced SQL: subqueries, CTEs, and window functions
4. Production-style ETL validation, incremental loads, and orchestration
