import math

def calculate_distance_with_coordinates(latitude_1, longitude_1, latitude_2, longitude_2):
    """ Function which calculates a distance between two geographic positions """
    earth_radius = 6373.0
    # Geographic points of the first place
    lat1 = math.radians(latitude_1)
    lon1 = math.radians(longitude_1)
    # Geographic points of the second place
    lat2 = math.radians(latitude_2)
    lon2 = math.radians(longitude_2)
    # Distance between the latitudes
    distance_longitude = lon2 - lon1
    # Distance between the longitudes
    distance_latitude = lat2 - lat1
    # Calculation of the distance with the Haversine formula
    a = math.sin(distance_latitude / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(distance_longitude / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = earth_radius * c
    return distance