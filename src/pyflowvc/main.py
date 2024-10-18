import json
import logging.config
import logging.handlers
from jsonlogger import settup_logging

logger = logging.getLogger("pyflowVC")


def bray_add(a, b):
    return a + b


def bray_add_two(a):
    return a + 2


def main():
    settup_logging()
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.critical("critical message")
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("exception message")


if __name__ == "__main__":
    main()
