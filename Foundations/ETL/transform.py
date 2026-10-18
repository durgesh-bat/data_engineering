import logging
from typing import Any

logger = logging.getLogger("etl.validation")


def transform_posts(
    posts: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Normalize API key userId to user_id and separate invalid records."""
    clean: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []

    for post in posts:
        post_id = post.get("id")
        user_id = post.get("userId")
        title = post.get("title")
        body = post.get("body")

        valid = (
            isinstance(post_id, int)
            and isinstance(user_id, int)
            and isinstance(title, str)
            and bool(title.strip())
            and isinstance(body, str)
            and bool(body.strip())
        )

        if not valid:
            rejected.append({
                "id": post_id,
                "reason": "Invalid id, userId, title, or body",
            })
            continue

        clean.append({
            "id": post_id,
            "user_id": user_id,
            "title": title.strip(),
            "body": body.strip(),
        })

    logger.info(
        "Transformation complete: clean=%s rejected=%s",
        len(clean),
        len(rejected),
    )
    return clean, rejected
