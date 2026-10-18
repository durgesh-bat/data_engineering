import logging
import os
from typing import Any

import psycopg
from dotenv import load_dotenv

logger = logging.getLogger("etl.load")
PROJECT_ROOT = __import__("pathlib").Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


def _connection_settings() -> dict[str, Any]:
    required = ("DB_HOST", "DB_PORT", "DB_NAME", "DB_USER", "DB_PASSWORD")
    missing = [key for key in required if not os.getenv(key)]
    if missing:
        raise RuntimeError(
            "Missing environment variables: " + ", ".join(missing)
            + ". Copy .env.example to .env and fill in local settings."
        )

    return {
        "host": os.environ["DB_HOST"],
        "port": int(os.environ["DB_PORT"]),
        "dbname": os.environ["DB_NAME"],
        "user": os.environ["DB_USER"],
        "password": os.environ["DB_PASSWORD"],
    }


def load_posts(posts: list[dict[str, Any]]) -> int:
    """UPSERT normalized post records into api_posts in one transaction."""
    if not posts:
        logger.info("No posts to load")
        return 0

    rows = [
        (post["id"], post["user_id"], post["title"], post["body"])
        for post in posts
    ]

    sql = """
        INSERT INTO api_posts (id, user_id, title, body)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (id) DO UPDATE SET
            user_id = EXCLUDED.user_id,
            title = EXCLUDED.title,
            body = EXCLUDED.body;
    """

    try:
        with psycopg.connect(**_connection_settings()) as conn:
            with conn.cursor() as cur:
                cur.executemany(sql, rows)

        logger.info("UPSERT transaction completed for %s posts", len(rows))
        return len(rows)

    except (psycopg.Error, KeyError, TypeError, ValueError):
        logger.exception("Post loading failed; transaction was rolled back")
        raise
