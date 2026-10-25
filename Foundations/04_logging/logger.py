"""Reusable logging practice example.

Run from the repository root:
    python Foundations/04_logging/logger.py
"""
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "Data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("etl")
logger.setLevel(logging.DEBUG)

custom_format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

if not logger.handlers:
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(custom_format)
    logger.addHandler(console_handler)

    file_handler = RotatingFileHandler(
        DATA_DIR / "etl.log",
        maxBytes=1024 * 1024,
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(custom_format)
    logger.addHandler(file_handler)


def main() -> None:
    api_logger = logging.getLogger("etl.api")
    api_logger.debug("Debug example: written to log file")
    api_logger.info("API example message")
    logger.warning("Warning example message")


if __name__ == "__main__":
    main()
