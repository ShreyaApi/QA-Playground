import logging
import os

os.makedirs("logs", exist_ok=True)


def get_logger():

    logger = logging.getLogger("QA-Playground")

    logger.setLevel(logging.INFO)

    if not logger.handlers:

        file_handler = logging.FileHandler("logs/automation.log", mode="a")

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger
