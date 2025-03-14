import geopandas as gpd
import numpy as np
import pytest
import shapely
from traitlets import TraitError

from lonboard import ScatterplotLayer


def test_accessor_length_validation():
    """Accessor length must match table length"""
    points = shapely.points([1, 2], [3, 4])
    gdf = gpd.GeoDataFrame(geometry=points)

    with pytest.raises(TraitError, match="same length as table"):
        _layer = ScatterplotLayer.from_geopandas(gdf, get_radius=np.array([1]))

    with pytest.raises(TraitError, match="same length as table"):
        _layer = ScatterplotLayer.from_geopandas(gdf, get_radius=np.array([1, 2, 3]))

    _layer = ScatterplotLayer.from_geopandas(gdf, get_radius=np.array([1, 2]))


def test_layer_fails_with_unexpected_argument():
    points = shapely.points([1, 2], [3, 4])
    gdf = gpd.GeoDataFrame(geometry=points)

    with pytest.raises(TypeError, match="unexpected keyword argument"):
        ScatterplotLayer.from_geopandas(gdf, unknown_keyword="foo")
