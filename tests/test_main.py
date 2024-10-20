import pytest
from unittest.mock import mock_open, patch, call
import meshio
from pyflowvc.main import write_coordinates, write_faces


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
    # mock_file().write.assert_any_call("0\n")
    # mock_file().write.assert_any_call("1\n")
    # mock_file().write.assert_any_call("2\n")
    # mock_file().write.assert_any_call("2\n")
    # mock_file().write.assert_any_call("3\n")
    # mock_file().write.assert_any_call("4\n")


if __name__ == "__main__":
    pytest.main()
