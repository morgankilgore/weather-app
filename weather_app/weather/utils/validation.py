
def is_valid_temperature_unit(unit):
    """
    Validates a temperature unit string

    Param(s):
        unit (str): Temperature unit string

    Returns: True if valid, else False
    """
    return unit.lower() in ['fahrenheit', 'celsius']


def is_valid_lat_lon(lat, lon):
    """
    Validates latitude and longitude coordinates

    Param(s):
        lat (float): Latitude coordinate
        lon (float): Longitude coordinate

    Returns: bool. True if valid, else False
    """
    try:
        lat = float(lat)
        lon = float(lon)
    except ValueError:
        return False
    return True


def is_valid_temperature_value(temp):
    """
    Validates if the provided temperature is a valid temperature

    Param(s):
        temp (float): Temperature

    Returns: bool. True if valid temperature value, else False
    """
    try:
        float(temp)
    except ValueError:
        return False
    return True


def is_valid_filters(filters):
    """
    Validates filters

    Param(s):
        filters (list): List of filters to validate

    Returns: bool. True if all filters are valid, else False
    """
    WEATHER_API_PROVIDERS = ['noaa', 'weather.com', 'accuweather']
    invalid_filters = list(set(filters) - set(WEATHER_API_PROVIDERS))
    if invalid_filters:
        return False
    return True
