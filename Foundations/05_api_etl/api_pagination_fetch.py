"""API pagination + validation + CSV load exercise.

Run from the repository root:
    python Foundations/05_api_etl/api_pagination_fetch.py
"""
import csv
import logging
import sys
import time
from pathlib import Path
from typing import Any

import requests

PROJECT_ROOT = Path(__file__).resolve().parents[2]
FOUNDATIONS_DIR = PROJECT_ROOT / "Foundations"
VALIDATION_DIR = FOUNDATIONS_DIR / "03_validation_exceptions"
if str(VALIDATION_DIR) not in sys.path:
    sys.path.insert(0, str(VALIDATION_DIR))

from data_validation import validate_title  # noqa: E402

API_URL = "https://jsonplaceholder.typicode.com/posts"
DATA_DIR = PROJECT_ROOT / "Data"
logger = logging.getLogger("etl.api_exercise")


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def fetch_page(page: int, limit: int = 10, max_attempts: int = 4) -> list[dict[str, Any]] | None:
    """Return a page, [] for an empty page, or None after request failure."""
    params = {"_page": page, "_limit": limit}
    for attempt in range(1, max_attempts + 1):
        try:
            response = requests.get(API_URL, params=params, timeout=10)
            response.raise_for_status()
            payload = response.json()
            if not isinstance(payload, list):
                logger.error("Page %s returned an unexpected response shape", page)
                return None
            return payload
        except requests.RequestException as exc:
            logger.warning("Page %s attempt %s/%s failed: %s", page, attempt, max_attempts, exc)
            if attempt < max_attempts:
                time.sleep(2 ** (attempt - 1))
    logger.error("Page %s failed after %s attempts", page, max_attempts)
    return None


def fetch_all_posts(limit: int = 10) -> list[dict[str, Any]] | None:
    if limit <= 0:
        raise ValueError("limit must be greater than zero")
    page = 1
    posts: list[dict[str, Any]] = []
    while True:
        data = fetch_page(page, limit)
        if data is None:
            return None
        if not data:
            return posts
        posts.extend(data)
        logger.info("Fetched page %s (%s records)", page, len(data))
        page += 1


def transform_posts(posts: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    clean: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    for post in posts:
        post_id = post.get("id")
        title = post.get("title")
        user_id = post.get("userId")
        is_valid, reason = validate_title(title)
        if is_valid and isinstance(post_id, int) and isinstance(user_id, int):
            clean.append({"id": post_id, "user_id": user_id, "title": title.strip()})
        else:
            rejected.append({"id": post_id, "reason": reason or "Invalid post id or userId"})
            logger.warning("Post %s rejected: %s", post_id, rejected[-1]["reason"])
    logger.info("Transform complete: clean=%s rejected=%s", len(clean), len(rejected))
    return clean, rejected


def save_csv(clean: list[dict[str, Any]], rejected: list[dict[str, Any]]) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    outputs = [
        (DATA_DIR / "clean_posts.csv", clean, ["id", "user_id", "title"]),
        (DATA_DIR / "rejected_posts.csv", rejected, ["id", "reason"]),
    ]
    for path, rows, fields in outputs:
        with path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
        logger.info("Saved %s rows to %s", len(rows), path)


def main() -> None:
    configure_logging()
    logger.info("API pagination practice started")
    posts = fetch_all_posts(limit=10)
    if posts is None:
        logger.error("Extraction failed; output files were not overwritten")
        raise SystemExit(1)
    clean, rejected = transform_posts(posts)
    save_csv(clean, rejected)
    logger.info("Done: raw=%s clean=%s rejected=%s", len(posts), len(clean), len(rejected))


if __name__ == "__main__":
    main()
