import pytest
from unittest.mock import mock_open, patch
import meshio
from pyflowvc.main import bray_add, write_coordinates


def test_bray_add():
    expected = 8
    actual = bray_add(3, 5)
    assert expected == actual


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


if __name__ == "__main__":
    pytest.main()
