import logging.config
import logging.handlers
from .jsonlogger import settup_logging

logger = logging.getLogger("pyflowVC")


def write_coordinates(mesh, coord_file):
    """Write coordinates (x, y, z) to the specified file."""
    with open(coord_file, "w") as f:
        for point in mesh.points:
            f.write(f"{point[0]}\n{point[1]}\n{point[2]}\n")


def main():
    settup_logging()


if __name__ == "__main__":
    main()
