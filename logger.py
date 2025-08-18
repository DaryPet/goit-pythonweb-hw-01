import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s:%(lineno)d — %(message)s",
)


def get_logger(name: str | None = None) -> logging.Logger:
    return logging.getLogger(name or "app")
