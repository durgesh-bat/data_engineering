-- Learning schema for a fresh data_engineering database.
-- Review before running against a database that already contains tables/data.

CREATE TABLE IF NOT EXISTS course (
    course_id INTEGER PRIMARY KEY,
    course_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INTEGER CHECK (age IS NULL OR age > 0),
    course VARCHAR(50),
    marks INTEGER CHECK (marks IS NULL OR (marks >= 0 AND marks <= 100)),
    course_id INTEGER REFERENCES course(course_id),
    email VARCHAR(100) UNIQUE,
    status VARCHAR(20) NOT NULL DEFAULT 'active'
);

CREATE TABLE IF NOT EXISTS api_posts (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    loaded_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO course (course_id, course_name)
VALUES
    (1, 'B.TECH'),
    (2, 'BBA'),
    (3, 'MCA'),
    (4, 'MBA'),
    (5, 'BCA')
ON CONFLICT (course_id) DO NOTHING;

INSERT INTO student (id, name, age, course, marks, course_id, email, status)
VALUES
    (102, 'RAHUL', 22, 'B.TECH', 100, 1, 'rahul102@example.com', 'active'),
    (103, 'PRIYA', 21, 'BBA', 62, 2, 'priya103@example.com', 'active'),
    (104, 'RAMESH', 25, 'MCA', 70, 3, 'ramesh104@example.com', 'active'),
    (105, 'RAJU', 26, 'MCA', 69, 3, 'raju105@example.com', 'active'),
    (106, 'RANI', 25, 'BCA', 89, 5, 'rani106@example.com', 'active'),
    (107, 'Aman', 22, 'MCA', 85, 3, 'aman107@example.com', 'active'),
    (108, 'Neha', 22, 'MCA', 88, 3, 'neha108@example.com', 'active'),
    (109, 'Karna', 23, 'BBA', 76, 2, 'karna109@example.com', 'active')
ON CONFLICT (id) DO NOTHING;
