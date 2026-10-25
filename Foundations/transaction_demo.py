
import logging
import os
from pathlib import Path
from psycopg.types.json import Jsonb
import psycopg
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s",
)

logger = logging.getLogger("etl.transaction")

settings = {
    "host": os.environ["DB_HOST"],
    "port": int(os.environ["DB_PORT"]),
    "dbname": os.environ["DB_NAME"],
    "user": os.environ["DB_USER"],
    "password": os.environ["DB_PASSWORD"],
}

records = [
    (9101, "First insert"),
    (9101, "Duplicate ID - reject this record"),
    (9102, "Third insert"),
    (9101, "Forth insert"),
    (9101, "Fifth insert"),
    (9102, "sixth insert"),
]

rejected_records = []

try:
    with psycopg.connect(**settings) as conn:
        with conn.cursor() as cur:

            # Clear only this dedicated practice table.
            cur.execute("DELETE FROM tx_demo")

            for record_id, note in records:
                cur.execute("SAVEPOINT one_record")

                try:
                    cur.execute(
                        """
                        INSERT INTO tx_demo (id, note)
                        VALUES (%s, %s)
                        """,
                        (record_id, note),
                    )

                except psycopg.errors.UniqueViolation as exc:
                    cur.execute("ROLLBACK TO SAVEPOINT one_record")
                    cur.execute("RELEASE SAVEPOINT one_record")

                    reason = "Duplicate primary key"

                    payload = {
                        "id": record_id,
                        "note": note,
                    }

                    rejected_records.append({
                        "id": record_id,
                        "reason": reason,
                    })

                    cur.execute(
                        """
                        INSERT INTO etl_rejected_records
                            (record_id, payload, reason,
                            pipeline_name, stage, error_type, status)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        """,
                        (
                            record_id,
                            Jsonb(payload),
                            reason,
                            "transaction_demo",
                            "database_load",
                            type(exc).__name__,
                            "pending",
                        ),
                    )

                    logger.warning(
                        "Rejected record id=%s: %s",
                        record_id,
                        reason,
                    )
                else:
                    cur.execute("RELEASE SAVEPOINT one_record")
                    logger.info("Inserted record id=%s", record_id)

            cur.execute("SELECT id, note FROM tx_demo ORDER BY id")
            saved_records = cur.fetchall()

    # Reaching here means the transaction committed successfully.
    print("Saved records:", saved_records)
    print("Rejected records:", rejected_records)

except psycopg.Error:
    logger.exception("Database transaction failed")
    raise
