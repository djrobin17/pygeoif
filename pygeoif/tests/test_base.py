"""Test Baseclass."""

import pytest

from pygeoif import geometry


def test_geometry_interface():
    """The geo interface must be implemented in subclasses."""
    base_geo = geometry._Geometry()

    with pytest.raises(NotImplementedError, match="^Must be implemented by subclass$"):
        assert base_geo.__geo_interface__


def test_bounds():
    """Subclasses must implement bounds."""
    base_geo = geometry._Geometry()
    with pytest.raises(NotImplementedError, match="^Must be implemented by subclass$"):

        assert base_geo.bounds


def test_wkt():
    """Implement wkt in subclasses."""
    base_geo = geometry._Geometry()
    with pytest.raises(NotImplementedError, match="^Must be implemented by subclass$"):

        assert base_geo.wkt


def test_wkt_inset():
    base_geo = geometry._Geometry()

    assert base_geo._wkt_inset == ""


def test_wkt_coordinates():
    base_geo = geometry._Geometry()
    with pytest.raises(NotImplementedError, match="^Must be implemented by subclass$"):

        assert base_geo._wkt_coords


def test_from_dict():
    base_geo = geometry._Geometry()
    with pytest.raises(NotImplementedError, match="^Must be implemented by subclass$"):

        assert base_geo._from_dict({"type": "_Geometry"})


def test_has_z():
    base_geo = geometry._Geometry()
    with pytest.raises(NotImplementedError, match="^Must be implemented by subclass$"):

        assert base_geo.has_z


def test_neq_no_interface():
    obj = object()
    base_geo = geometry._Geometry()

    assert base_geo != obj


def test_convex_hull():
    base_geo = geometry._Geometry()
    with pytest.raises(NotImplementedError, match="^Must be implemented by subclass$"):

        assert base_geo.convex_hull()
