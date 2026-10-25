# File and Program Catalogue

Run commands from the repository root unless a section says otherwise. Some early exercises intentionally use local input files or retain exploratory code; read the notes before running them.

## Foundations

### 00 — Overview
- `Foundations/00_overview/data_ingestion.md`: definition and high-level source-to-destination flow.

### 01 — Python basics
- `Foundations/01_python_basics/dictionary.py`: list of student dictionaries, top student, average, filtering.
- `Foundations/01_python_basics/lab.py`: empty scratchpad for new exercises.
- Run: `python Foundations/01_python_basics/dictionary.py`.

### 02 — Files and formats
- `Foundations/02_files_csv_json/file_handling.py`: reading/writing/appending text and processing lines. Legacy demo expects a local `students.txt`.
- `Foundations/02_files_csv_json/csv_file_manipulation.py`: CSV DictReader/DictWriter, filters and aggregates; expects `Data/Students.csv`.
- `Foundations/02_files_csv_json/json_manipulation.py`: JSON strings/files, nested records, transformation; expects input files under `Data/`.
- The referenced example input files are local exercises and are not committed.

### 03 — Validation and exceptions
- `Foundations/03_validation_exceptions/data_validation.py`: names, ages, marks, and title validation.
- `Foundations/03_validation_exceptions/exception_handling.py`: malformed numeric values, skip bad records, and collect invalid rows; expects `Data/Students_dirty.csv`.

### 04 — Logging
- `Foundations/04_logging/logger.py`: named loggers, handlers, formatting, rotating file output.
- Run: `python Foundations/04_logging/logger.py`. Output logs go to ignored `Data/etl.log`.

### 05 — API and ETL exercises
- `Foundations/05_api_etl/server_users.py`: fetch user API records and print a summary.
- `Foundations/05_api_etl/fetch_and_clean.py`: normalize user fields and save JSON.
- `Foundations/05_api_etl/api_pagination_fetch.py`: paginated posts, retries/backoff, validation, clean/rejected CSVs.
- These exercises require internet access to JSONPlaceholder and write outputs under ignored `Data/`.

### 06 — SQL and PostgreSQL
- `Foundations/06_sql_postgresql/SQL_PROGRESS.md`: completed and pending SQL topics.
- `Foundations/06_sql_postgresql/SQL_RECALL.md`: joins, filtering, aggregation, NULL, grouping recall sheet.
- `sql/01_schema.sql`: student/course/API-posts practice schema.
- `sql/02_index_lab.sql`: optional one-million-row index demo; uses disk space.

### 07 — Python + PostgreSQL (Psycopg 3)
- `Foundations/07_python_postgresql/01_connection/db_connect.py`: connect and query server version.
- `Foundations/07_python_postgresql/02_fetching/read_students.py`: SELECT and print rows.
- `Foundations/07_python_postgresql/02_fetching/fetch_methods_demo.py`: compare fetchone/fetchmany/fetchall.
- `Foundations/07_python_postgresql/03_parameterized_queries/search_student.py`: parameterized lookup using %s and ILIKE.
- `Foundations/07_python_postgresql/04_writing/insert_many_students.py`: executemany and conflict handling.
- `Foundations/07_python_postgresql/05_transactions/transaction_demo.py`: SAVEPOINT, per-record rejection, JSONB payload logging.
- `Foundations/07_python_postgresql/06_retry_policy/retry_policy_demo.py`: retryable vs non-retryable SQLSTATE demo.
- Notes: `Foundations/07_python_postgresql/notes/Python_PostgreSQL_Lessons_01_02.md` and the same basename with `.docx`.

The database exercises use the root `.env`. The transaction demo also needs the practice tables `tx_demo` and `etl_rejected_records` from the transaction lesson.

## Integrated ETL project

The current API-to-PostgreSQL project lives in `projects/api_to_postgres_etl/`:
- `main.py` orchestrates.
- `extract.py` performs API extraction, retries, pagination.
- `transform.py` validates and normalizes records.
- `load.py` performs a PostgreSQL UPSERT.
- `logger_config.py` configures console/file logs.

Run: `python projects/api_to_postgres_etl/main.py`. It expects PostgreSQL table `api_posts` from `sql/01_schema.sql`.

## Notes and planning
- `docs/LEARNING_NOTES.md`: multi-topic notes.
- `docs/ROADMAP.md`: current checkpoint and future path.
- `docs/REPOSITORY_STRUCTURE.md`: folder purpose and conventions.
- `docs/glossary.md`: terminology.
- `docs/archive/learning_roadmap_original.txt`: preserved original roadmap.
- `Foundations/README.md`: index to numbered learning folders.

## Rules for future files
1. Small lessons go under the matching numbered `Foundations/` topic.
2. Integrated multi-file projects go under `projects/<project_name>/`.
3. SQL schema/labs go under top-level `sql/`.
4. Add every new program to this catalogue, including purpose and run command.
5. Update the roadmap when the active lesson changes.
6. Never commit `.env`, credentials, virtualenvs, generated output, or logs.
