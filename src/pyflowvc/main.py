import json
import logging.config
import logging.handlers
import pathlib

logger = logging.getLogger("pyflowVC")


def settup_logging():
    config_file = pathlib.Path("logging_configs/config.json")
    with open(config_file) as f_in:
        config = json.load(f_in)
    logging.config.dictConfig(config)


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
