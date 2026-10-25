# Repository Structure and Future Organization

## Principle

Organize by **learning topic first**, then by reusable project. Keep small, focused lessons separate from integrated pipelines. Every new program should have a short explanation, a stable run command, and a link from the catalogue.

## Current structure

The existing files are kept at their current paths for now to avoid breaking the user's local Debian working copy and older scripts that rely on relative imports/data paths.

- `Foundations/*.py`: early Python practice programs
- `Foundations/ETL/*.py`: PostgreSQL integration exercises plus the complete API-to-PostgreSQL ETL modules
- `Foundations/Notes/`: lesson notes in Markdown and Word
- `sql/`: database schema and index experiments
- `Server/`: early API-user exercise
- `SQL.txt`: quick SQL/JOIN recall sheet
- `Learning_RoadMap.dat`: original roadmap source; the maintained roadmap is now `docs/ROADMAP.md`

Use [FILE_CATALOG.md](FILE_CATALOG.md) to map the current file names to topics.

## Target structure for a safe future migration

This is the target design; it is **not yet the actual on-disk layout**.

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
│   └── lessons/
├── foundations/
│   ├── python/
│   │   ├── basics/
│   │   ├── files_csv_json/
│   │   ├── validation_exceptions/
│   │   ├── logging/
│   │   └── api_pagination/
│   ├── sql/
│   └── postgres_integration/
│       ├── connection_queries/
│       ├── inserts_updates/
│       ├── transactions_savepoints/
│       └── retries_idempotency/
├── projects/
│   └── api_to_postgres_etl/
│       ├── main.py
│       ├── extract.py
│       ├── transform.py
│       ├── load.py
│       ├── logger_config.py
│       └── tests/
├── sql/
│   ├── schema/
│   └── labs/
├── data/
│   ├── sample/       # small fake/sanitized data only
│   └── output/       # ignored by Git
└── tests/
```

## Rules for future additions

1. **One file, one learning purpose.** For example, keep CSV reading and PostgreSQL connections in separate small exercises.
2. **Preserve runnable examples.** Document the exact command and expected input files in the file catalogue.
3. **Avoid import side effects.** Put executable demo code under `if __name__ == "__main__":`.
4. **Use stable paths.** Resolve source/data paths from `Path(__file__)` rather than relying on whichever directory the shell is currently in.
5. **Separate exercises from projects.** A demo is a foundation exercise; a project orchestrates multiple modules.
6. **Keep secrets out of Git.** Commit `.env.example`, never real `.env`.
7. **Add tests as behavior becomes stable.** Begin with validators and pure transformation functions, then database integration tests.
8. **Update documentation as part of every change.** Include the program in `FILE_CATALOG.md`, note progress in `ROADMAP.md`, and update the README if the entry point changes.
9. **Prefer small commits.** One focused topic or one path migration per commit makes reviewing and rollback easier.
10. **Migrate paths only after checking imports.** The old scripts include imports such as `from logger import logger` and relative data paths; moving them without updating those details will break them.

## Migration order

1. Finish and stabilize the Python/PostgreSQL integration lessons.
2. Add tests/guards/path fixes to older Python exercises.
3. Move pure Python examples into topic folders.
4. Move PostgreSQL labs into dedicated topic folders.
5. Move the integrated ETL into `projects/api_to_postgres_etl/`.
6. Update run commands, then verify from a fresh clone on Debian.
