# Data Engineering Learning Roadmap

This is the canonical roadmap for the repository. Update the status after each completed lesson. The goal is durable learning through small runnable examples, not speed.

## Current position

**Active track:** Python + PostgreSQL integration, revising from the basics.

- [x] Lesson 1 — connect Python to PostgreSQL with Psycopg 3
- [x] Lesson 2 — connection, cursor, `execute()`, and basic `SELECT`
- [ ] Lesson 3 — `fetchone()`, `fetchmany()`, `fetchall()` (**current**)
- [ ] Lesson 4 — parameterized queries with `%s`
- [ ] Lesson 5 — `INSERT`, `UPDATE`, `DELETE` from Python
- [ ] Lesson 6 — multiple parameter sets with `executemany()`
- [ ] Lesson 7 — connection contexts and transaction boundaries
- [ ] Lesson 8 — exception handling, logging, and `raise`
- [ ] Lesson 9 — SAVEPOINT and per-record failure handling
- [ ] Lesson 10 — rejected/quarantine records with payload and status
- [ ] Lesson 11 — UPSERT and idempotency
- [ ] Lesson 12 — retry classification and operation safety
- [ ] Lesson 13 — bulk loading with PostgreSQL COPY
- [ ] Lesson 14 — integrate and test the complete API-to-PostgreSQL ETL

## Completed foundations

### Python
- Variables, data types, collections, dictionaries, nested records, loops, conditions, functions
- File handling: read, write, append, and line-by-line processing
- CSV reader/writer and dictionary-based CSV operations
- JSON strings, objects, and files
- Input validation, exceptions, and record-level error handling
- Logging levels, loggers, handlers, formatters, and rotating logs

### API and ETL
- HTTP GET with timeout and status checking
- Pagination, bounded retries, and backoff
- Transforming API records into a consistent schema
- Separating valid and rejected records
- Extract → Transform/Validate → Load workflow
- API-to-PostgreSQL loading with UPSERT

### SQL/PostgreSQL
- SELECT, WHERE, logical conditions, BETWEEN, ORDER BY, LIMIT
- INSERT, UPDATE, DELETE, and transaction basics
- COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING, DISTINCT, NULL
- INNER/LEFT/RIGHT JOINs
- PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, CHECK, DEFAULT
- Indexes, EXPLAIN, EXPLAIN ANALYZE, Seq/Index/Bitmap scans, composite indexes

See [SQL progress](../Foundations/SQL_PROGRESS.md), [general notes](../Foundations/LEARNING_NOTES.md), and the [file catalogue](FILE_CATALOG.md).

## Future curriculum

### Stage A — finish Python/PostgreSQL integration
1. Cursor fetching methods and result shape
2. Parameterized SQL and SQL injection prevention
3. CRUD and RETURNING
4. Multi-row inserts, transactions, error propagation
5. SAVEPOINT, error quarantine, retry-safe processing
6. Idempotent loading and UPSERT
7. COPY and batch performance
8. Automated tests and load metrics

### Stage B — SQL depth (after integration practice)
1. CASE WHEN and conditional aggregation
2. Subqueries and correlated subqueries
3. CTEs (`WITH`) and recursive CTEs
4. Window functions: ROW_NUMBER, RANK, LAG, LEAD
5. Set operations: UNION, INTERSECT, EXCEPT
6. Views and materialized views
7. Normalization, schema design, and query optimization

### Stage C — production-style ETL
- Data quality rules and documented schemas
- Raw, clean, and rejected layers
- Incremental loads and change detection
- Idempotency, retries, checkpoints, and recovery
- Structured logging, metrics, and alerting
- Unit/integration tests

### Stage D — modern Data Engineering
1. Linux/Bash and Git workflows
2. Data warehousing: OLTP vs OLAP, facts/dimensions, star schema, SCD
3. Apache Spark/PySpark, partitions, shuffles, Spark SQL
4. Orchestration with Airflow: DAGs, scheduling, retries, dependencies
5. One cloud provider first (AWS recommended in the current plan)
6. Docker, Kafka, CI/CD, and Terraform basics

## Learning workflow

For each topic:
1. Read the short note.
2. Run the example on Debian.
3. Change one thing and observe the behavior.
4. Explain the output in your own words.
5. Save the final code/note and update this roadmap.

Keep the current lesson here accurate so learning can resume after a break.
