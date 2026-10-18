# Data Engineering Learning Notes

This file summarizes the concepts covered so far in the guided learning project. Examples are educational and intentionally compact.

## Python foundations

### Core concepts covered
- Variables, strings, integers, floats, booleans, lists, dictionaries, and lists of dictionaries
- `if/else`, loops, functions, parameters, return values
- Common pitfalls: returning from inside a loop accidentally, `list.append()` returning `None`, and using built-in names such as `sum` as variables
- Type hints and basic input validation

### File handling
- `with open(...)` for reliable file closure
- Modes: `r` read, `w` overwrite, `a` append
- Read files line-by-line when large files should not be loaded fully into memory
- Use `strip()` when trimming whitespace/newlines

### CSV and JSON
- CSV: `csv.reader`, `csv.DictReader`, `csv.writer`, `csv.DictWriter`, `writeheader()`
- JSON: `json.load()` / `json.dump()` work with files; `json.loads()` / `json.dumps()` work with strings
- Avoid double serializing JSON unless a string containing JSON is deliberately required

### Exceptions and validation
- Use `try/except` around operations that can fail
- Catch specific errors such as `ValueError`, `FileNotFoundError`, and `requests.RequestException`
- Keep invalid records separate from a pipeline/system failure
- A useful contract is `None` for an extraction failure and `[]` for a successful empty result
- When a validator returns a tuple like `(is_valid, reason)`, unpack it: `is_valid, reason = validate_record(record)`

## REST API extraction

Practice endpoint: `https://jsonplaceholder.typicode.com/posts`

Concepts practiced:
- HTTP methods: GET, POST, PUT, PATCH, DELETE
- `requests.get(..., timeout=10)`, `response.raise_for_status()`, `response.json()`
- Pagination through `_page` and `_limit`
- Use `extend()` to append all items from a page, and stop when a successful page is empty
- Retry failed requests with bounded attempts and a backoff delay
- Avoid silently treating a failed page as a successful empty result

Typical flow:

```text
API request
  -> timeout/status handling
  -> retry
  -> pagination
  -> raw records
```

## Logging

Covered:
- Logger, handler, formatter, and levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
- Logger level and handler level both affect which messages appear
- Console output plus rotating file logging via `RotatingFileHandler`
- Child loggers such as `etl.api` can propagate to the configured `etl` parent logger
- Avoid attaching duplicate handlers repeatedly

The current reusable setup is in `Foundations/ETL/logger_config.py`.

## ETL concepts

ETL means Extract, Transform, Load.

- **Extract:** retrieve raw records from an API, file, or other source.
- **Transform:** normalize fields, validate data, and separate invalid records.
- **Load:** persist accepted data to a destination such as CSV or PostgreSQL.

Previous learning flow:

```text
JSONPlaceholder API
  -> retry + timeout + pagination
  -> transformation and validation
  -> CSV output
```

Current runnable flow:

```text
JSONPlaceholder API
  -> retry + timeout + pagination
  -> normalize userId to user_id and validate
  -> Psycopg 3 parameterized UPSERT
  -> PostgreSQL api_posts
```

## PostgreSQL and SQL concepts covered

### Query foundations
- `SELECT`, column selection, `WHERE`, comparisons, `AND`, `OR`, `BETWEEN`
- `ORDER BY`, `LIMIT`
- `INSERT`, `UPDATE`, `DELETE`
- Difference between `DELETE`, `TRUNCATE`, and `DROP`

### Aggregation and grouping
- `COUNT`, `AVG`, `MAX`, `MIN`, `SUM`
- `GROUP BY`, `HAVING`, `DISTINCT`
- `COUNT(column)` ignores NULL values; with a `LEFT JOIN`, `COUNT(child.id)` is usually more appropriate than `COUNT(*)` for counting matching children

### NULL, joins, and constraints
- Use `IS NULL` / `IS NOT NULL`, not `= NULL`
- INNER JOIN returns matches; LEFT JOIN preserves every left-side row; RIGHT JOIN preserves every right-side row
- Constraints practiced: PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, CHECK, DEFAULT
- A primary key guarantees uniqueness and non-null values; PostgreSQL creates an index to support it
- A foreign key does not automatically create an index on the referencing column in PostgreSQL
- Normal UNIQUE constraints in PostgreSQL generally allow multiple NULL values

### Transactions
- `BEGIN`, `COMMIT`, `ROLLBACK`
- If many changes belong to one transaction and an error causes a rollback, those uncommitted changes are undone
- Data committed in an earlier transaction remains committed
- Psycopg connection contexts commit on successful exit and roll back if an exception escapes the context

## Indexes and query plans

Practiced:
- Primary key indexes and manually created indexes
- `CREATE INDEX`, `ANALYZE`, `EXPLAIN`, `EXPLAIN ANALYZE`
- `Seq Scan`, `Index Scan`, `Bitmap Index Scan`, and `Bitmap Heap Scan`
- Index availability does not guarantee the planner will use the index; it chooses a plan using estimated costs and table statistics
- Small tables often favor sequential scans
- Composite index order matters; `(course_id, marks)` is especially suited to queries that constrain the leading `course_id` and optionally filter/range on `marks`
- A separate `marks` index may suit queries filtering only `marks`, though a sequential scan may still be cheapest for a low-selectivity query

Run the optional reproducible lab in `sql/02_index_lab.sql`. It creates one-million-row demo tables and uses disk space.

## Python + PostgreSQL (Psycopg 3)

### Connection and cursor
- Connection (`conn`) manages database session/transaction
- Cursor (`cur`) executes statements and fetches query results
- `cur.execute(sql, params)` runs a statement with parameters
- `fetchone()` returns one row or `None`
- `fetchall()` returns all remaining rows, not rows already fetched

### Parameterized SQL
Use placeholders rather than concatenating user-provided values:

```python
cur.execute(
    "SELECT id, name FROM student WHERE id = %s",
    (102,),
)
row = cur.fetchone()
```

For a one-element tuple, the comma in `(102,)` is required. Do not quote the `%s` placeholder.

### Multiple inserts and UPSERT
- `executemany()` runs a statement over multiple parameter sets
- Use `ON CONFLICT (id) DO NOTHING` to skip primary-key conflicts
- Use `ON CONFLICT (id) DO UPDATE SET ... = EXCLUDED...` to update existing rows
- Re-running an UPSERT for the same stable IDs avoids duplicate rows, but true idempotency also depends on side effects and the overall pipeline design
- `executemany()` is not a replacement for PostgreSQL `COPY` for every high-volume workload; bulk loading will be studied separately

### Current scripts
- `Foundations/ETL/db_connect.py`: test the connection
- `Foundations/ETL/search_student.py`: safe parameterized search
- `Foundations/ETL/insert_many_students.py`: multi-row insert with conflict-ignore
- `Foundations/ETL/main.py`: end-to-end API-to-PostgreSQL ETL
- `Foundations/ETL/extract.py`: API retry and pagination
- `Foundations/ETL/transform.py`: normalization and validation
- `Foundations/ETL/load.py`: transactional PostgreSQL UPSERT

## Next lessons

1. Finish the transaction rollback practice (one transaction vs committed batches)
2. Improve ETL exception handling and load metrics
3. Compare `executemany()` with PostgreSQL `COPY`
4. Continue SQL later with subqueries, CTEs, window functions, and query optimization
5. Move on to Spark/PySpark after these integration fundamentals
