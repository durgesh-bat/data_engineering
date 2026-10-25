# Data Engineering Learning Repository

A hands-on, code-first learning repository for Python, SQL, PostgreSQL, APIs, ETL, and database integration. The repository preserves the original learning exercises while documenting what each file teaches and how the project will grow.

## Start here

1. **[Learning roadmap](docs/ROADMAP.md)** — what is covered, current lesson, and what comes next.
2. **[File and program catalogue](docs/FILE_CATALOG.md)** — find each program by topic.
3. **[Repository structure and future organization](docs/REPOSITORY_STRUCTURE.md)** — current layout and planned target layout.
4. **[Python + PostgreSQL Lessons 1–2 notes](Foundations/Notes/Python_PostgreSQL_Lessons_01_02.md)** — connection, cursor, `execute()`, and basic SELECT.
5. **[SQL progress](Foundations/SQL_PROGRESS.md)** and [general learning notes](Foundations/LEARNING_NOTES.md).

## Current learning status

The current learning track is revisiting **Python + PostgreSQL integration** from the beginning, at a careful pace.

- Lesson 1: connect Python to PostgreSQL using Psycopg 3.
- Lesson 2: connection, cursor, `execute()`, and reading rows.
- Lesson 3 (current): `fetchone()`, `fetchmany()`, and `fetchall()`.
- Upcoming: parameterized SQL, INSERT/UPDATE/DELETE, multiple inserts, transactions, error handling, SAVEPOINT, rejected-record handling, retry safety, and bulk loading.

Earlier hands-on work includes Python fundamentals, CSV/JSON, API pagination/retries, logging, PostgreSQL joins/aggregates/constraints/indexes, and a JSONPlaceholder API-to-PostgreSQL ETL.

## Current repository layout

```text
data_engineering/
├── README.md
├── requirements.txt
├── .env.example
├── docs/
│   ├── ROADMAP.md
│   ├── FILE_CATALOG.md
│   └── REPOSITORY_STRUCTURE.md
├── Foundations/
│   ├── Notes/
│   │   ├── Python_PostgreSQL_Lessons_01_02.md
│   │   └── Python_PostgreSQL_Lessons_01_02.docx
│   ├── ETL/
│   │   ├── db_connect.py
│   │   ├── read_students.py
│   │   ├── fetch_methods_demo.py
│   │   ├── search_student.py
│   │   ├── insert_many_students.py
│   │   ├── extract.py
│   │   ├── transform.py
│   │   ├── load.py
│   │   ├── logger_config.py
│   │   └── main.py
│   ├── API_Pagination_Fetch.py
│   ├── Fetch_and_clean.py
│   ├── File_Handling.py
│   ├── CSV_File_Manipulation.py
│   ├── Json_Manipulation.py
│   ├── Data_Validation.py
│   ├── ExceptionHandling.py
│   ├── dictionary.py
│   ├── logger.py
│   ├── transaction_demo.py
│   └── retry_policy_demo.py
├── Server/
│   └── server.py
└── sql/
    ├── 01_schema.sql
    └── 02_index_lab.sql
```

See the file catalogue for the exact purpose and recommended run location of each program. Some original exercises use relative data paths and may expect the working directory to be `Foundations/`; consult the catalogue before running them. Some exercises also execute demonstration code at module import time, so treat them as learning examples rather than reusable library modules.

## Setup on Debian/Linux

```bash
git clone https://github.com/durgesh-bat/data_engineering.git
cd data_engineering
sudo apt update
sudo apt install python3 python3-venv python3-pip postgresql postgresql-client -y
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` with your own local PostgreSQL settings. Do not commit `.env`, passwords, tokens, virtual environments, generated datasets, or logs.

If your repository is already cloned, update it with:

```bash
git pull --ff-only origin main
```

If Git reports local/untracked-file conflicts, stop and back up those files before trying cleanup commands.

## PostgreSQL setup

Use an administrative psql session to create a database/user if you do not already have them, then load the schema:

```bash
psql -h localhost -U de_user -d data_engineering -f sql/01_schema.sql
```

The schema script is intended for a learning database. Review it before using it on any database containing important data.

## Run the current integration lesson

From the repository root:

```bash
python Foundations/ETL/db_connect.py
python Foundations/ETL/read_students.py
python Foundations/ETL/fetch_methods_demo.py
```

For the API-to-PostgreSQL ETL:

```bash
python Foundations/ETL/main.py
```

The ETL uses JSONPlaceholder as a public practice API. A successful full extraction commonly yields 100 posts. The loader UPSERTs by post ID, making repeated runs avoid duplicate IDs.

## SQL and index lab

- Schema/sample tables: `sql/01_schema.sql`
- One-million-row index demonstrations: `sql/02_index_lab.sql`

The index lab creates large demo tables and consumes disk space. Run it only in a practice database.

## Working agreements for this learning repo

- Keep each lesson small: concept → runnable example → exercise → short notes.
- Put durable explanations in Markdown and, when useful, export a companion Word document under `Foundations/Notes/`.
- Add or update the file catalogue when adding a new program.
- Update `docs/ROADMAP.md` whenever a lesson is completed or the current lesson changes.
- Never commit passwords, tokens, local `.env`, virtual environments, logs, or generated output.
- Preserve the original learning exercises; refactor them only when the lesson requires it and keep a note of behavior changes.
