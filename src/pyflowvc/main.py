import logging.config
import logging.handlers
from .jsonlogger import settup_logging
import argparse
import meshio

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
    """
    Main function to extract mesh data (coordinates, faces, and velocity)
    from a .vtu file and write them to separate files.

    This function can be run from the command line with the following options:

    - The input .vtu file is mandatory.
    - Optionally, the output files for coordinates, faces, and velocity can be
      specified. If not provided, default file names will be used.

    Command-line arguments:
    - --coordinates: File to write coordinates data (default: coordinates.txt).
    - --faces: File to write faces data (default: faces.txt).
    - --velocity: File to write velocity data (default: velocity.txt).

    Example usage:
    python extract_mesh_data.py input_file.vtu --coordinates custom_coords.txt --faces custom_faces.txt --velocity custom_velocity.txt

    If no custom output files are provided, the default files:
    coordinates.txt, faces.txt, and velocity.txt are used.

    """

    parser = argparse.ArgumentParser(
        description="Extract mesh data from a .vtu file and write to separate files."
    )
    parser.add_argument("input_file", help="The input .vtu file to read.")
    parser.add_argument(
        "--coordinates", default="coordinates.txt", help="Output file for coordinates."
    )
    parser.add_argument("--faces", default="faces.txt", help="Output file for faces.")
    parser.add_argument(
        "--velocity", default="velocity.txt", help="Output file for velocity."
    )

    args = parser.parse_args()

    # Read the mesh data from the input .vtu file
    mesh = meshio.read(args.input_file)

    # Write coordinates, faces, and velocity to their respective files
    write_coordinates(mesh, args.coordinates)
    write_faces(mesh, args.faces)
    write_velocity(mesh, args.velocity)


if __name__ == "__main__":
    settup_logging()
    main()
