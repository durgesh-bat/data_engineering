# Data Engineering Learning Repository

A hands-on, code-first workspace for Python, SQL/PostgreSQL, APIs, ETL, and database integration.

## Start here

1. [Foundations index](Foundations/README.md) — topic folders and programs.
2. [Roadmap](docs/ROADMAP.md) — completed topics, current lesson, and future curriculum.
3. [Program catalogue](docs/FILE_CATALOG.md) — what each program teaches and how to run it.
4. [Repository structure](docs/REPOSITORY_STRUCTURE.md) — organization rules and future growth.
5. [General learning notes](docs/LEARNING_NOTES.md).
6. [Glossary](docs/glossary.md).

## Current learning checkpoint

We are revising **Python + PostgreSQL integration** from the beginning:
- Lessons 1–2: connect with Psycopg 3, connection/cursor, `execute()`, basic SELECT.
- Lesson 3 (current): `fetchone()`, `fetchmany()`, and `fetchall()`.
- Next: parameterized SQL, CRUD, multi-row inserts, transactions, SAVEPOINT, rejected records, retry safety, and bulk loading.

## Organized layout

```text
data_engineering/
├── README.md
├── .env.example
├── requirements.txt
├── docs/
│   ├── ROADMAP.md
│   ├── FILE_CATALOG.md
│   ├── REPOSITORY_STRUCTURE.md
│   ├── LEARNING_NOTES.md
│   ├── glossary.md
│   └── archive/learning_roadmap_original.txt
├── Foundations/
│   ├── README.md
│   ├── 00_overview/
│   ├── 01_python_basics/
│   ├── 02_files_csv_json/
│   ├── 03_validation_exceptions/
│   ├── 04_logging/
│   ├── 05_api_etl/
│   ├── 06_sql_postgresql/
│   └── 07_python_postgresql/
├── Server/
├── projects/
│   └── api_to_postgres_etl/
└── sql/
    ├── 01_schema.sql
    └── 02_index_lab.sql
```

## Debian/Linux setup

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

Fill in local PostgreSQL values in `.env`. Never commit `.env`, real credentials, virtual environments, generated files, or logs.

If the repository is already cloned, update it with:

```bash
git pull --ff-only origin main
```

If Git reports a local/untracked-file conflict, stop and back up the file before running cleanup commands.

## Run the current integration lesson

From the repository root:

```bash
python Foundations/07_python_postgresql/01_connection/db_connect.py
python Foundations/07_python_postgresql/02_fetching/read_students.py
python Foundations/07_python_postgresql/02_fetching/fetch_methods_demo.py
```

## Run the integrated ETL project

```bash
python projects/api_to_postgres_etl/main.py
```

The pipeline extracts posts from JSONPlaceholder, validates/transforms records, and UPSERTs them into PostgreSQL's `api_posts` table.

## Learning/repository rules

- Small one-topic programs belong in the matching numbered `Foundations/` folder.
- Complete multi-module pipelines belong in `projects/<project_name>/`.
- SQL schemas and repeatable SQL labs belong in top-level `sql/`.
- Update the catalogue and roadmap when adding a new lesson.
- Old exercises may require local sample inputs; see the catalogue before running them.
