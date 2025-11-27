import json
from importlib.resources import files

from shapely.geometry import Point, shape

geojson_path = files("is_in_iran.data").joinpath("iran.geojson")

with geojson_path.open("r", encoding="utf-8") as f:
    geojson = json.load(f)

iran_geom = shape(geojson["features"][0]["geometry"])


def is_in_iran(lat: float, lon: float) -> bool:
    """
    Check if the given (lat, lon) is inside Iran.

    Parameters
    ----------
    lat : float
        Latitude in degrees.
    lon : float
        Longitude in degrees.

    Returns
    -------
    bool
        True if the point is in (or on the border of) Iran, False otherwise.
    """
    point = Point(lon, lat)  # GeoJSON: [lon, lat]
    return iran_geom.contains(point) or iran_geom.touches(point)
