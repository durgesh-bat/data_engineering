import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")

settings = {
    "host": os.environ["DB_HOST"],
    "port": int(os.environ["DB_PORT"]),
    "dbname": os.environ["DB_NAME"],
    "user": os.environ["DB_USER"],
    "password": os.environ["DB_PASSWORD"],
}


def main() -> None:
    with psycopg.connect(**settings) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, name, marks
                FROM student
                ORDER BY id;
            """)

            rows = cur.fetchall()
            for row in rows:
                print(row)


if __name__ == "__main__":
    main()
