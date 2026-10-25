"""Basic user API exercise: fetch users and print a small summary.

Run from repository root:
    python Foundations/05_api_etl/server_users.py
"""
import logging
from typing import Any

import requests

API_URL = "https://jsonplaceholder.typicode.com/users"
logger = logging.getLogger("etl.users_api")


def fetch_users() -> list[dict[str, Any]] | None:
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        payload = response.json()
    except requests.RequestException:
        logger.exception("User API request failed")
        return None

    if not isinstance(payload, list):
        logger.error("User API returned an unexpected response shape")
        return None
    return payload


def print_users(users: list[dict[str, Any]]) -> None:
    for user in users:
        address = user.get("address") or {}
        print(f"{user.get('name')} -> {user.get('email')} -> {address.get('city')}")


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
    users = fetch_users()
    if users is None:
        raise SystemExit(1)
    print(f"Fetched {len(users)} users")
    print_users(users)


if __name__ == "__main__":
    main()
