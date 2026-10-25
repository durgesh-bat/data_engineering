# API → PostgreSQL ETL Project

This is the integrated project, separate from small Foundation exercises.

- `main.py`: orchestrates the workflow.
- `extract.py`: HTTP requests, timeout, retries, pagination.
- `transform.py`: validation and field normalization (`userId` → `user_id`).
- `load.py`: transactional PostgreSQL UPSERT using Psycopg 3.
- `logger_config.py`: console and rotating-file logs.

Run from repository root after configuring `.env` and applying `sql/01_schema.sql`:

```bash
python projects/api_to_postgres_etl/main.py
```

The target table is `api_posts`; JSONPlaceholder `/posts` is the public practice source. The loader uses the stable post ID with `ON CONFLICT ... DO UPDATE` so repeated runs do not create duplicate IDs.
