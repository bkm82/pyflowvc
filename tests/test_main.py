import pytest
from unittest.mock import mock_open, patch, call
import meshio
import argparse
from pyflowvc.main import write_coordinates, write_faces, write_velocity
from pyflowvc.main import main as pyflowvcmain


@pytest.fixture
def mock_mesh():
    """Fixture to create a mock mesh object"""
    return meshio.Mesh(
        points=[[0.0, 1.0, 2.0], [3.0, 4.0, 5.0]],
        cells=[("triangle", [[0, 1, 2], [2, 3, 4]])],
        point_data={"velocity": [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]},
    )


@patch("builtins.open", new_callable=mock_open)
def test_write_coordinates(mock_file, mock_mesh):
    """Test writing the cordinates of the file."""
    # Call the function with the mock mesh
    write_coordinates(mock_mesh, "coordinates.txt")

    # Assert the file was written correctly
    # Assert the file was written correctly
    mock_file().write.assert_any_call("0.0\n1.0\n2.0\n")
    mock_file().write.assert_any_call("3.0\n4.0\n5.0\n")


@patch("builtins.open", new_callable=mock_open)
def test_write_faces(mock_file, mock_mesh):
    """Test writing face data to file."""
    # Call the function with the mock mesh
    write_faces(mock_mesh, "faces.txt")

    expected_calls = [
        call("0\n"),
        call("1\n"),
        call("2\n"),
        call("2\n"),
        call("3\n"),
        call("4\n"),
    ]
    mock_file().write.assert_has_calls(expected_calls)


@patch("builtins.open", new_callable=mock_open)
def test_write_velocity(mock_file, mock_mesh):
    """Test writing velocity data to file."""
    # Call the function with the mock mesh
    write_velocity(mock_mesh, "velocity.txt")

    # Assert the file was written correctly
    mock_file().write.assert_any_call("1.0\n2.0\n3.0\n")
    mock_file().write.assert_any_call("4.0\n5.0\n6.0\n")


@patch("builtins.open", new_callable=mock_open)
@patch("meshio.read")
@patch(
    "argparse.ArgumentParser.parse_args",
    return_value=argparse.Namespace(
        input_file="mock.vtu",
        coordinates="coordinates.txt",
        faces="faces.txt",
        velocity="velocity.txt",
    ),
)
def test_main_with_defaults(mock_args, mock_read, mock_file, mock_mesh):
    """Test the main function with default file names."""
    mock_read.return_value = mock_mesh
    # Call the main function (this will parse the mocked sys.argv)
    pyflowvcmain()

    # Check if meshio.read was called with the correct file
    mock_read.assert_called_once_with("mock.vtu")

    # Check if the correct file names were used
    mock_file.assert_any_call("coordinates.txt", "w")
    mock_file.assert_any_call("faces.txt", "w")
    mock_file.assert_any_call("velocity.txt", "w")

    # Check if the correct data was written for coordinates
    expected_coords_calls = [call("0.0\n1.0\n2.0\n"), call("3.0\n4.0\n5.0\n")]
    mock_file().write.assert_has_calls(expected_coords_calls, any_order=False)

    # Check if the correct data was written for faces
    expected_faces_calls = [
        call("0\n"),
        call("1\n"),
        call("2\n"),
        call("2\n"),
        call("3\n"),
        call("4\n"),
    ]
    mock_file().write.assert_has_calls(expected_faces_calls, any_order=False)

    # Check if the correct data was written for velocity
    expected_velocity_calls = [call("1.0\n2.0\n3.0\n"), call("4.0\n5.0\n6.0\n")]
    mock_file().write.assert_has_calls(expected_velocity_calls, any_order=False)


if __name__ == "__main__":
    pytest.main()
