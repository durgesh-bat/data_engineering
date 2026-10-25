# Repository Structure

## Actual organized layout

```text
data_engineering/
├── README.md
├── requirements.txt
├── .env.example
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
├── projects/
│   └── api_to_postgres_etl/
└── sql/
    ├── 01_schema.sql
    └── 02_index_lab.sql
```

## Folder responsibilities

- `Foundations/00_overview/`: first principles and vocabulary.
- `Foundations/01_python_basics/`: core syntax, collections, small functions.
- `Foundations/02_files_csv_json/`: files and common data formats.
- `Foundations/03_validation_exceptions/`: validators and exception handling.
- `Foundations/04_logging/`: logging concepts and reusable example.
- `Foundations/05_api_etl/`: small API and ETL exercises.
- `Foundations/06_sql_postgresql/`: SQL recall sheets and learning progress.
- `Foundations/07_python_postgresql/`: progressively harder Psycopg lessons.
- `projects/`: complete, multi-module pipelines.
- `sql/`: reproducible schemas and database experiments.
- `docs/`: roadmap, catalogue, general notes, and glossary.

## Future rules

1. Keep one-topic exercises in the matching Foundation folder.
2. Put integrated pipelines under `projects/<project_name>/`.
3. Keep secrets in local `.env` only; commit just `.env.example`.
4. Store generated files/logs under the ignored `Data/` directory.
5. Add new programs to `docs/FILE_CATALOG.md`.
6. Update `docs/ROADMAP.md` after each lesson.
7. Avoid import-time side effects; put demo execution under `if __name__ == "__main__":`.
8. Prefer `Path(__file__)` for paths so programs behave consistently when run from the repository root.
9. Move/rename files only after updating imports and checking the program can run from a fresh clone.

## Future additions (when needed)

- `tests/`: unit and integration tests.
- `data/sample/`: small, sanitized input datasets safe to commit.
- `projects/<name>/tests/`: tests for an integrated project.
- `docs/lessons/`: long-form handouts.

Do not create folders until there is a real use for them; keep the repository understandable.
