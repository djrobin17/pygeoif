"""Test LineString."""
from unittest import mock

import pytest

from pygeoif import exceptions
from pygeoif import geometry


def test_coords_get2d():
    line = geometry.LineString([(0, 0), (1, 1)])

    assert line.coords == ((0.0, 0.0), (1.0, 1.0))


def test_coords_get_3d():
    line = geometry.LineString([(0, 0, 0), (1, 1, 1)])

    assert line.coords == ((0.0, 0.0, 0), (1.0, 1.0, 1))


def test_coords_set2d():
    line = geometry.LineString([(0, 0), (1, 2)])  # pragma: no mutate
    line.coords = ((0.0, 0.0), (1.0, 1.0))

    assert line.coords == ((0.0, 0.0), (1.0, 1.0))


def test_coords_set_3d():
    line = geometry.LineString([(0, 0), (1, 0)])  # pragma: no mutate
    line.coords = ((0.0, 0.0, 0), (1.0, 1.0, 1))

    assert line.coords == ((0.0, 0.0, 0), (1.0, 1.0, 1))


def test_set_geoms_raises():
    line = geometry.LineString([(0, 0), (1, 0)])  # pragma: no mutate

    with pytest.raises(
        exceptions.DimensionError,
        match="^All coordinates must have the same dimension$",
    ):
        line._set_geoms([(0.0, 0.0, 0), (1.0, 1.0)])  # pragma: no mutate


def test_geo_interface():
    line = geometry.LineString([(0, 0), (1, 1)])

    assert line.__geo_interface__ == {
        "type": "LineString",
        "bbox": (0.0, 0.0, 1.0, 1.0),  # pragma: no mutate
        "coordinates": ((0.0, 0.0), (1.0, 1.0)),
    }


def test_bounds():
    line = geometry.LineString([(0, 0), (1, 1)])

    assert line.bounds == (0.0, 0.0, 1.0, 1.0)


def test_bounds3d():
    line = geometry.LineString([(0, 0, 0), (1, 1, 3), (2, 2, 6)])  # pragma: no mutate

    assert line.bounds == (0.0, 0.0, 2.0, 2.0)  # pragma: no mutate


def test_wkt():
    line = geometry.LineString([(0, 0), (1, 1), (2, 2)])

    assert line.wkt == "LINESTRING (0 0, 1 1, 2 2)"


def test_wkt3d():
    line = geometry.LineString([(0, 0, 0), (1, 1, 3), (2, 2, 6)])

    assert line.wkt == "LINESTRING Z (0 0 0, 1 1 3, 2 2 6)"


def test_from_dict():
    line = geometry.LineString._from_dict(
        {
            "type": "LineString",
            "bbox": (0.0, 0.0, 1.0, 1.0),  # pragma: no mutate
            "coordinates": ((0.0, 0.0), (1.0, 1.0)),
        },
    )

    assert line.coords == ((0.0, 0.0), (1.0, 1.0))


def test_from_compatible():
    not_a_geometry = mock.Mock(
        __geo_interface__={
            "type": "LineString",
            "coordinates": ((0.0, 0.0, 1.0), (1.0, 1.0, 2.0)),
        },
    )
    line = geometry.LineString._from_interface(not_a_geometry)
    assert line.coords == ((0.0, 0.0, 1.0), (1.0, 1.0, 2.0))


def test_repr2d():
    line = geometry.LineString([(0, 0), (1, 1), (2, 2)])

    assert repr(line) == "LineString(((0, 0), (1, 1), (2, 2)))"


def test_repr3d():
    line = geometry.LineString([(0, 0, 0), (1, 1, 3), (2, 2, 6)])

    assert repr(line) == "LineString(((0, 0, 0), (1, 1, 3), (2, 2, 6)))"


def test_repr_eval():
    line = geometry.LineString([(0, 0, 0), (1, 1, 3), (2, 2, 6)])

    assert (
        eval(repr(line), {}, {"LineString": geometry.LineString}).__geo_interface__
        == line.__geo_interface__
    )


def test_has_z_2d():
    line = geometry.LineString([(0, 0), (1, 1), (2, 2)])

    assert not line.has_z


def test_has_z_3d():
    line = geometry.LineString([(0, 0, 0), (1, 1, 3), (2, 2, 6)])

    assert line.has_z


def test_from_points():
    p1 = geometry.Point(0, 0)
    p2 = geometry.Point(1, 1)

    line = geometry.LineString.from_points(p1, p2)

    assert line.coords == ((0, 0), (1, 1))


def test_from_points_3d():
    p1 = geometry.Point(0, 0, 1)
    p2 = geometry.Point(1, 1, 2)

    line = geometry.LineString.from_points(p1, p2)

    assert line.coords == ((0, 0, 1), (1, 1, 2))


def test_from_points_mixed():
    p1 = geometry.Point(0, 0, 1)
    p2 = geometry.Point(1, 1)

    with pytest.raises(exceptions.DimensionError):
        geometry.LineString.from_points(p1, p2)
