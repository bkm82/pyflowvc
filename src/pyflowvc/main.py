import logging.config
import logging.handlers
from .jsonlogger import settup_logging

logger = logging.getLogger("pyflowVC")


def bray_add(a, b):
    return a + b


def bray_add_two(a):
    return a + 2


def write_coordinates(mesh, coord_file):
    """Write cordinates (x, y, z) to the specified file"""
    pass


def main():
    settup_logging()


if __name__ == "__main__":
    main()
