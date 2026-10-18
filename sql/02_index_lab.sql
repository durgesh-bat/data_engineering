-- OPTIONAL LAB: creates two 1,000,000-row tables.
-- Run only in a practice database and be mindful of disk space.
-- After each index change, run ANALYZE and inspect EXPLAIN output.

DROP TABLE IF EXISTS student_demo;
CREATE TABLE student_demo AS
SELECT
    gs AS id,
    ((gs - 1) % 10) + 1 AS course_id,
    ((gs * 37) % 101) AS marks
FROM generate_series(1, 1000000) AS gs;

ANALYZE student_demo;

-- Baseline: likely Seq Scan / Parallel Seq Scan.
EXPLAIN
SELECT *
FROM student_demo
WHERE course_id = 3 AND marks >= 70;

-- Composite index: equality on first key and range on second key.
CREATE INDEX idx_student_demo_course_marks
ON student_demo(course_id, marks);
ANALYZE student_demo;

EXPLAIN
SELECT *
FROM student_demo
WHERE course_id = 3 AND marks >= 70;

EXPLAIN
SELECT *
FROM student_demo
WHERE course_id = 3;

EXPLAIN
SELECT *
FROM student_demo
WHERE marks >= 70;

-- Add a separate marks index and compare the plan.
CREATE INDEX idx_student_demo_marks
ON student_demo(marks);
ANALYZE student_demo;

EXPLAIN
SELECT *
FROM student_demo
WHERE marks >= 70;

-- Change query to EXPLAIN ANALYZE to observe actual execution statistics.
-- Then compare index order by creating a second index:
CREATE INDEX idx_student_demo_marks_course
ON student_demo(marks, course_id);
ANALYZE student_demo;

EXPLAIN
SELECT *
FROM student_demo
WHERE marks >= 70 AND course_id = 3;

-- Single-column index demo, mirroring our name-index lesson.
DROP TABLE IF EXISTS index_demo;
CREATE TABLE index_demo AS
SELECT
    gs AS id,
    'Student ' || gs AS name
FROM generate_series(1, 1000000) AS gs;

ALTER TABLE index_demo ADD PRIMARY KEY (id);
ANALYZE index_demo;

EXPLAIN
SELECT * FROM index_demo WHERE id = 900000;

EXPLAIN
SELECT * FROM index_demo WHERE name = 'Student 900000';

CREATE INDEX idx_index_demo_name ON index_demo(name);
ANALYZE index_demo;

EXPLAIN
SELECT * FROM index_demo WHERE name = 'Student 900000';
