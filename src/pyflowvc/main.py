import logging.config
import logging.handlers
from .jsonlogger import settup_logging

logger = logging.getLogger("pyflowVC")


def write_coordinates(mesh, coord_file):
    """Write coordinates (x, y, z) to the specified file."""
    with open(coord_file, "w") as f:
        for point in mesh.points:
            f.write(f"{point[0]}\n{point[1]}\n{point[2]}\n")


def write_faces(mesh, filename):
    """
    Writes the faces (vertex indices) of the mesh to a file,
    with each vertex index on a new line.
    """
    with open(filename, "w") as file:
        # Access the faces (cells) that are triangular
        for cell_block in mesh.cells:
            if cell_block.type == "triangle":
                for face in cell_block.data:
                    for vertex in face:
                        file.write(f"{vertex}\n")


def write_velocity(mesh, velocity_file):
    """Write velocity (x, y, z) for each point to the specified file."""
    if "velocity" in mesh.point_data:
        with open(velocity_file, "w") as f:
            for velocity in mesh.point_data["velocity"]:
                f.write(f"{velocity[0]}\n{velocity[1]}\n{velocity[2]}\n")
    else:
        print("No velocity data found in the .vtu file.")


def main():
    settup_logging()


if __name__ == "__main__":
    main()
