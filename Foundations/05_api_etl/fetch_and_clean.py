"""Fetch user records, normalize selected fields, and save JSON.

Run from the repository root:
    python Foundations/05_api_etl/fetch_and_clean.py
"""
import json
import logging
from pathlib import Path
from typing import Any

import requests

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "Data"
API_URL = "https://jsonplaceholder.typicode.com/users"
logger = logging.getLogger("etl.users")


def fetch_users() -> list[dict[str, Any]] | None:
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        payload = response.json()
    except requests.RequestException:
        logger.exception("Could not fetch users from API")
        return None
    if not isinstance(payload, list):
        logger.error("API returned unexpected JSON shape")
        return None
    return payload


def transform_users(users: list[dict[str, Any]]) -> list[dict[str, Any]]:
    cleaned = []
    for user in users:
        address = user.get("address") or {}
        name, email, city = user.get("name"), user.get("email"), address.get("city")
        if not all(isinstance(value, str) and value.strip() for value in (name, email, city)):
            logger.warning("Skipping user id=%s: missing name, email, or city", user.get("id"))
            continue
        cleaned.append({
            "id": user.get("id"),
            "name": name.strip(),
            "email": email.strip(),
            "city": city.strip(),
        })
    return cleaned


def save_users(users: list[dict[str, Any]]) -> Path:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    output = DATA_DIR / "users_clean.json"
    with output.open("w", encoding="utf-8") as file:
        json.dump(users, file, indent=2, ensure_ascii=False)
    logger.info("Saved %s users to %s", len(users), output)
    return output


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
    users = fetch_users()
    if users is None:
        raise SystemExit(1)
    save_users(transform_users(users))


if __name__ == "__main__":
    main()
