# File and Program Catalogue

Use this page to find a program by topic. The older exercises are intentionally preserved; not every early exercise is production-ready or safe to import as a module.

## Python foundations

| Topic | Program | What it practices | Notes |
|---|---|---|---|
| Collections / list of dictionaries | [dictionary.py](../Foundations/dictionary.py) | Student dictionaries, top student, average, filtering | Small in-memory example |
| General scratch lab | [lab.py](../Foundations/lab.py) | Scratchpad | Currently empty |
| File handling | [File_Handling.py](../Foundations/File_Handling.py) | Read, write, append, process line-based records | Uses local text files and relative paths |
| CSV | [CSV_File_Manipulation.py](../Foundations/CSV_File_Manipulation.py) | DictReader/DictWriter, average, filtering, write CSV | Expects sample data relative to current working directory |
| JSON | [Json_Manipulation.py](../Foundations/Json_Manipulation.py) | dump/load, lists of dictionaries, transforming nested JSON | References local data files |
| Validation | [Data_Validation.py](../Foundations/Data_Validation.py) | Name, age, marks, title validators | Contains reusable functions and examples |
| Exceptions | [ExceptionHandling.py](../Foundations/ExceptionHandling.py) | Handle malformed CSV values and continue | Some demo calls run at module level |
| Logging | [logger.py](../Foundations/logger.py) | Logger, handlers, formatter, propagation | Early learning example; ETL uses a separate shared config |

## API, pagination, and ETL practice

| Topic | Program | What it practices | Notes |
|---|---|---|---|
| User API demo | [Server/server.py](../Server/server.py) | GET users, inspect JSON, transform and save fields | Calls the API and writes output when run |
| API cleanup exercises | [Fetch_and_clean.py](../Foundations/Fetch_and_clean.py) | User records, transformation, saving JSON | Imports the server example; contains legacy experimental code |
| API pagination and validation | [API_Pagination_Fetch.py](../Foundations/API_Pagination_Fetch.py) | Page/limit, retries, logging, clean/rejected CSVs | Learning prototype; check before rerunning because it writes output files |

## Python ↔ PostgreSQL integration

| Topic | Program | What it practices |
|---|---|---|
| Connection/version | [db_connect.py](../Foundations/ETL/db_connect.py) | Connect with Psycopg and execute a query |
| SELECT and rows | [read_students.py](../Foundations/ETL/read_students.py) | Read rows and print tuples |
| Fetch behavior | [fetch_methods_demo.py](../Foundations/ETL/fetch_methods_demo.py) | `fetchone()`, `fetchmany()`, `fetchall()` on one result set |
| Parameterized lookup | [search_student.py](../Foundations/ETL/search_student.py) | Use `%s` parameters and `ILIKE` |
| Multiple inserts | [insert_many_students.py](../Foundations/ETL/insert_many_students.py) | `executemany()`, conflict handling |
| Transaction / SAVEPOINT lab | [transaction_demo.py](../Foundations/transaction_demo.py) | Per-record savepoints, duplicate rejection, JSONB payload logging |
| Retry policy lab | [retry_policy_demo.py](../Foundations/retry_policy_demo.py) | SQLSTATE classification and retry decisions |

Run the current fetching lesson from the repository root:

```bash
source .venv/bin/activate
python Foundations/ETL/fetch_methods_demo.py
```

## End-to-end API → PostgreSQL project

| File | Responsibility |
|---|---|
| [main.py](../Foundations/ETL/main.py) | Orchestrates extraction, transformation, and loading |
| [extract.py](../Foundations/ETL/extract.py) | Requests, timeouts, retries, pagination |
| [transform.py](../Foundations/ETL/transform.py) | Normalizes `userId` to `user_id`, validates payload fields |
| [load.py](../Foundations/ETL/load.py) | PostgreSQL UPSERT using Psycopg 3 |
| [logger_config.py](../Foundations/ETL/logger_config.py) | Shared console and rotating-file logging |

Run from the repository root:

```bash
python Foundations/ETL/main.py
```

## SQL and database assets

| File | Purpose |
|---|---|
| [SQL.txt](../SQL.txt) | SQL + JOIN recall notes: joins, filters, aggregates, NULL, grouping |
| [01_schema.sql](../sql/01_schema.sql) | Practice schema and sample course/student rows |
| [02_index_lab.sql](../sql/02_index_lab.sql) | Optional million-row index experiment; consumes disk space |
| [SQL_PROGRESS.md](../Foundations/SQL_PROGRESS.md) | Completed SQL topics and future SQL syllabus |

## Durable notes

- [Python + PostgreSQL Lessons 1–2 (Markdown)](../Foundations/Notes/Python_PostgreSQL_Lessons_01_02.md)
- [Python + PostgreSQL Lessons 1–2 (Word)](../Foundations/Notes/Python_PostgreSQL_Lessons_01_02.docx)
- [General learning notes](../Foundations/LEARNING_NOTES.md)
- [SQL progress](../Foundations/SQL_PROGRESS.md)
- [Roadmap](ROADMAP.md)

## Future file placement rules

- Short single-topic practice: keep under `Foundations/` and add it to this catalogue.
- Reusable PostgreSQL integration exercises: `Foundations/ETL/` for now; future migration plan is documented in [REPOSITORY_STRUCTURE.md](REPOSITORY_STRUCTURE.md).
- Complete end-to-end pipelines: `projects/<project_name>/` after the path migration is planned.
- SQL schema and reproducible SQL labs: `sql/`.
- Long-form lesson notes: `Foundations/Notes/` for the moment.
- Secrets, `.env`, virtual environments, generated data, and logs must never be committed.

## Known cleanup items for later

- Some early scripts execute code at import time; add `if __name__ == "__main__":` guards before reusing them as modules.
- Standardize data paths using `Path(__file__)` or a documented project-root convention.
- Review the legacy API exercise's imports and error handling.
- Decide whether `Learning_RoadMap.dat` and the oddly named `Foundations/?` should be archived after their content is preserved in canonical Markdown docs.
