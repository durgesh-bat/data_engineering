
import logging
import os
import time
from pathlib import Path

import psycopg
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s",
)

logger = logging.getLogger("etl.retry")

settings = {
    "host": os.environ["DB_HOST"],
    "port": int(os.environ["DB_PORT"]),
    "dbname": os.environ["DB_NAME"],
    "user": os.environ["DB_USER"],
    "password": os.environ["DB_PASSWORD"],
}

# SQLSTATE codes for errors that may be transient.
RETRYABLE_SQLSTATES = {
    "40001",  # Serialization failure
    "40P01",  # Deadlock detected
}


def is_retryable(exc: psycopg.Error) -> bool:
    state = exc.sqlstate

    if state in RETRYABLE_SQLSTATES:
        return True

    # Class 08 represents connection exceptions.
    return state is not None and state.startswith("08")


def run_with_retry(operation, max_attempts=3):
    for attempt in range(1, max_attempts + 1):
        try:
            with psycopg.connect(**settings) as conn:
                with conn.cursor() as cur:
                    operation(cur)

            logger.info("Operation successful")
            return

        except psycopg.Error as exc:
            if not is_retryable(exc):
                logger.error(
                    "Permanent/non-retryable database error: "
                    "SQLSTATE=%s, error=%s",
                    exc.sqlstate,
                    exc,
                )
                raise

            if attempt == max_attempts:
                logger.error(
                    "All %s attempts failed",
                    max_attempts,
                )
                raise

            delay = 2 ** (attempt - 1)

            logger.warning(
                "Attempt %s failed; retrying in %s second(s)",
                attempt,
                delay,
            )

            time.sleep(delay)


def duplicate_insert(cur):
    # This should conflict if id=9101 exists in tx_demo.
    cur.execute(
        "INSERT INTO tx_demo (id, note) VALUES (%s, %s)",
        (9101, "Retry policy test"),
    )


if __name__ == "__main__":
    try:
        run_with_retry(duplicate_insert)
    except psycopg.Error:
        logger.info(
            "Demo finished: duplicate error was not retried."
        )
