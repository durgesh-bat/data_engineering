import logging

from extract import fetch_all_posts
from logger_config import configure_logging
from load import load_posts
from transform import transform_posts

logger = logging.getLogger("etl")


def main() -> None:
    configure_logging()
    logger.info("ETL pipeline started")

    raw_posts = fetch_all_posts(limit=10)
    if raw_posts is None:
        logger.error("Pipeline stopped: extraction failed; no data loaded")
        raise SystemExit(1)

    clean_posts, rejected_posts = transform_posts(raw_posts)

    loaded_count = load_posts(clean_posts)

    logger.info(
        "ETL pipeline completed: raw=%s clean=%s rejected=%s processed_for_load=%s",
        len(raw_posts),
        len(clean_posts),
        len(rejected_posts),
        loaded_count,
    )

    if rejected_posts:
        logger.warning("Rejected records: %s", rejected_posts[:10])


if __name__ == "__main__":
    main()
