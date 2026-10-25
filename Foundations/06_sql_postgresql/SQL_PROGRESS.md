# SQL Learning Progress

## Covered with PostgreSQL practice

- `SELECT`, selecting columns, `WHERE`, comparisons, `AND`, `OR`, `BETWEEN`
- `ORDER BY`, `LIMIT`
- `INSERT`, `UPDATE`, `DELETE`; difference between `DELETE`, `TRUNCATE`, and `DROP`
- Transactions: `BEGIN`, `COMMIT`, `ROLLBACK`
- Aggregates: `COUNT`, `AVG`, `MAX`, `MIN`, `SUM`
- `GROUP BY`, `HAVING`, `DISTINCT`, NULL handling
- `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, join + aggregates
- Constraints: primary key, foreign key, unique, not-null, check, default
- Indexes and query plans: `EXPLAIN`, `EXPLAIN ANALYZE`, sequential/index/bitmap scans
- Single-column and composite index experiments; leftmost-prefix intuition

## Topics to continue later

- Subqueries and correlated subqueries
- CTEs (`WITH`) and recursive CTEs
- `CASE WHEN`, conditional aggregation
- Window functions: `ROW_NUMBER`, `RANK`, `LAG`, `LEAD`
- Set operators: `UNION`, `INTERSECT`, `EXCEPT`
- Views and materialized views
- Schema normalization and design
- Deeper query optimization

## Useful concepts to remember

- A primary key is a constraint, not merely a column named `id`; PostgreSQL creates a unique index to enforce it.
- PostgreSQL does not automatically create an index on the referencing side of every foreign key.
- An index being available does not guarantee the planner will use it.
- `EXPLAIN` shows the estimated plan; `EXPLAIN ANALYZE` executes the statement and adds actual timing/row statistics.
- Composite-index column order matters. Equality on the leading column followed by a range on the next column is a common useful pattern.
- On very small tables, a sequential scan can be cheaper than using an index.
