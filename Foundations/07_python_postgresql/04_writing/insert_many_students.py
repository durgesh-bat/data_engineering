import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[3]
load_dotenv(PROJECT_ROOT / ".env")


def main() -> None:
    students = [
        (108, "Neha", 22, "MCA", 88, 3, "neha108@example.com"),
        (109, "Karna", 23, "BBA", 76, 2, "karna109@example.com"),
    ]

    settings = {
        "host": os.environ["DB_HOST"],
        "port": int(os.environ["DB_PORT"]),
        "dbname": os.environ["DB_NAME"],
        "user": os.environ["DB_USER"],
        "password": os.environ["DB_PASSWORD"],
    }

    with psycopg.connect(**settings) as conn:
        with conn.cursor() as cur:
            cur.executemany(
                """
                INSERT INTO student
                    (id, name, age, course, marks, course_id, email)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING;
                """,
                students,
            )

    print(f"Processed {len(students)} student rows (conflicts are skipped).")


if __name__ == "__main__":
    main()
