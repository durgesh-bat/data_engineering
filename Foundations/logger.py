import logging
from logging.handlers import RotatingFileHandler


logger = logging.getLogger("etl")
logger.setLevel(logging.DEBUG)


custom_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(custom_format)
logger.addHandler(console_handler)


file_handler = RotatingFileHandler(
    "Data/etl.log",
    maxBytes=1024 * 1024,
    backupCount=3
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(custom_format)
logger.addHandler(file_handler)


# AFTER handlers are configured
api_logger = logging.getLogger("etl.api")
api_console = logging.StreamHandler()
api_console.setLevel(logging.INFO)
api_console.setFormatter(custom_format)

api_logger.addHandler(api_console)
api_logger.propagate = False

api_logger.info(f"API test message and api_logger.propagate: {api_logger.propagate}")