import logging
import os

# Create logs folder if it doesn't exist
os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("PlaywrightLogger")

logger.setLevel(logging.INFO)

# Prevent duplicate logs
if not logger.handlers:

    file_handler = logging.FileHandler(
        "logs/automation.log",
        mode="a"
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)