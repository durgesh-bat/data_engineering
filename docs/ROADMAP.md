# Data Engineering Learning Roadmap

The roadmap is the source of truth for where learning resumes after a break. Use a small loop: concept → runnable example → exercise → notes.

## Current checkpoint

**Active track: Python + PostgreSQL integration (revision).**

- [x] Lesson 1 — connect Python to PostgreSQL with Psycopg 3
- [x] Lesson 2 — connection, cursor, `execute()`, and basic SELECT
- [ ] Lesson 3 — `fetchone()`, `fetchmany()`, and `fetchall()` (**current**)
- [ ] Lesson 4 — parameterized SQL with `%s`
- [ ] Lesson 5 — INSERT, UPDATE, DELETE, RETURNING
- [ ] Lesson 6 — `executemany()` and multiple records
- [ ] Lesson 7 — transaction boundaries, COMMIT, ROLLBACK
- [ ] Lesson 8 — exceptions, logging, and `raise`
- [ ] Lesson 9 — SAVEPOINT and record-level recovery
- [ ] Lesson 10 — rejected/quarantine records with payload and status
- [ ] Lesson 11 — UPSERT and idempotency
- [ ] Lesson 12 — retry classification and operation safety
- [ ] Lesson 13 — PostgreSQL COPY/bulk loading
- [ ] Lesson 14 — end-to-end API-to-PostgreSQL ETL review

## Completed foundations

### Python
Variables, collections, loops, conditions, functions, file handling, CSV/JSON, validation, exception handling, and logging.

### API and ETL
HTTP requests, timeouts, pagination, bounded retries, backoff, transformation/validation, rejected records, Extract → Transform → Load, and API-to-PostgreSQL UPSERT.

### SQL/PostgreSQL
SELECT/WHERE/ORDER BY/LIMIT, DML, transactions, aggregates, GROUP BY/HAVING, DISTINCT/NULL, INNER/LEFT/RIGHT JOIN, constraints, indexes, EXPLAIN, and composite-index experiments.

See [general notes](LEARNING_NOTES.md), [SQL progress](../Foundations/06_sql_postgresql/SQL_PROGRESS.md), [SQL recall](../Foundations/06_sql_postgresql/SQL_RECALL.md), and [program catalogue](FILE_CATALOG.md).

## Future curriculum

### Stage A — finish Python/PostgreSQL integration
1. Fetch methods and result shapes
2. Parameterized SQL and SQL injection prevention
3. CRUD and RETURNING
4. Batch inserts, transactions, exception propagation
5. SAVEPOINT and per-record recovery
6. Rejection/quarantine and retry design
7. UPSERT/idempotency
8. COPY, load metrics, and tests

### Stage B — advanced SQL
- CASE WHEN and conditional aggregation
- Subqueries and correlated subqueries
- CTEs and recursive CTEs
- Window functions: ROW_NUMBER, RANK, LAG, LEAD
- UNION, INTERSECT, EXCEPT
- Views, materialized views, normalization, query optimization

### Stage C — production-style ETL
Data-quality contracts, raw/clean/rejected layers, incremental loads, checkpoints, retries, alerting, unit/integration tests.

### Stage D — modern Data Engineering
Linux/Bash/Git, data warehousing, Spark/PySpark, Airflow, one cloud provider first (AWS is the current plan), Docker, Kafka, CI/CD, Terraform.

## Repository maintenance

After completing a lesson, update this file and its relevant note. Keep this checkpoint current so learning can resume after time away.
