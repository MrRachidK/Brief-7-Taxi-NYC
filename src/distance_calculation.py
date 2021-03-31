import math

def calculate_distance_with_coordinates(entry, lat1_value, lon1_value, lat2_value, lon2_value):
    """ Function which calculates a distance between two geographic positions """
    earth_radius = 6373.0
    # Geographic points of the first place
    lat1 = math.radians(entry[lat1_value])
    lon1 = math.radians(entry[lon1_value])
    # Geographic points of the second place
    lat2 = math.radians(entry[lat2_value])
    lon2 = math.radians(entry[lon2_value])
    # Distance between the latitudes
    distance_longitude = lon2 - lon1
    # Distance between the longitudes
    distance_latitude = lat2 - lat1
    # Calculation of the distance with the Haversine formula
    a = math.sin(distance_latitude / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(distance_longitude / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = round(earth_radius * c, ndigits=2)
    return distance