import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


def main() -> None:
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    settings = {
        "host": os.environ["DB_HOST"],
        "port": int(os.environ["DB_PORT"]),
        "dbname": os.environ["DB_NAME"],
        "user": os.environ["DB_USER"],
        "password": os.environ["DB_PASSWORD"],
    }

    with psycopg.connect(**settings) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id, name, marks
                FROM student
                WHERE name ILIKE %s
                ORDER BY id;
                """,
                (name,),
            )
            rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No matching students found.")


if __name__ == "__main__":
    main()
