import logging
import time
from typing import Any

import requests

logger = logging.getLogger("etl.api")
API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_page(page: int, limit: int = 10, retries: int = 3) -> list[dict[str, Any]] | None:
    """Fetch one page. Return None for request failure, [] for a valid empty page."""
    params = {"_page": page, "_limit": limit}

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(API_URL, params=params, timeout=10)
            response.raise_for_status()
            payload = response.json()

            if not isinstance(payload, list):
                logger.error("Page %s returned unexpected JSON shape", page)
                return None

            return payload

        except (requests.RequestException, ValueError) as exc:
            logger.warning(
                "Page %s attempt %s/%s failed: %s",
                page,
                attempt,
                retries,
                exc,
            )
            if attempt < retries:
                time.sleep(attempt)  # simple backoff for learning purposes

    logger.error("Page %s failed after %s attempts", page, retries)
    return None


def fetch_all_posts(limit: int = 10) -> list[dict[str, Any]] | None:
    """Fetch all pages. None means a page failed; [] means no posts were returned."""
    if limit <= 0:
        raise ValueError("limit must be greater than zero")

    page = 1
    all_posts: list[dict[str, Any]] = []

    while True:
        data = fetch_page(page=page, limit=limit)

        if data is None:
            logger.error("Extraction stopped because page %s failed", page)
            return None

        if not data:
            break

        logger.info("Fetched page %s (%s records)", page, len(data))
        all_posts.extend(data)
        page += 1

    logger.info("Extraction complete: %s posts", len(all_posts))
    return all_posts
