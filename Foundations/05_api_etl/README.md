# API and ETL Exercises

- `server_users.py`: fetch users and display a summary.
- `fetch_and_clean.py`: normalize user fields and save JSON.
- `api_pagination_fetch.py`: paginated posts extraction, retries/backoff, validation, clean/rejected CSV outputs.

Run from repository root:

```bash
python Foundations/05_api_etl/server_users.py
python Foundations/05_api_etl/fetch_and_clean.py
python Foundations/05_api_etl/api_pagination_fetch.py
```

These exercises require internet access to JSONPlaceholder. Output goes to ignored `Data/`. Importing the modules will not call the API; network execution is guarded by `main()`.
