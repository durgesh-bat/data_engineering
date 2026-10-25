# Python + PostgreSQL (Psycopg 3)

Progress through these folders in order:

1. `01_connection/db_connect.py` — connect and query PostgreSQL version.
2. `02_fetching/read_students.py` — SELECT and print rows.
3. `02_fetching/fetch_methods_demo.py` — `fetchone()`, `fetchmany()`, `fetchall()`.
4. `03_parameterized_queries/search_student.py` — parameterized lookup using `%s` and `ILIKE`.
5. `04_writing/insert_many_students.py` — `executemany()` and conflict handling.
6. `05_transactions/transaction_demo.py` — SAVEPOINT and rejection logging.
7. `06_retry_policy/retry_policy_demo.py` — retryable/non-retryable database errors.

Notes: [Lessons 1–2 Markdown](notes/Python_PostgreSQL_Lessons_01_02.md) and [Word](notes/Python_PostgreSQL_Lessons_01_02.docx).

Run commands from the repository root with `.venv` activated and a configured root `.env`. The transaction example requires the practice tables `tx_demo` and `etl_rejected_records`.
