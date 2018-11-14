from weather_app.settings import WEATHER_API_URL
from weather.utils.request import post_request
from weather.utils.validation import is_valid_temperature_unit, is_valid_lat_lon


class WeatherDotCom(object):
    def __init__(self):
        self.url = '{}/weatherdotcom'.format(WEATHER_API_URL)

    def get_current_temp(self, lat, lon, unit='fahrenheit'):
        """
        Gets current temperature

        Param(s):
            lat (float): Latitude of the location to get the current temperature from
            log (float): Longitude of the location to get the current temperature from
            unit (str): Temperature unit.

        Returns: tuple(bool, str).  (True, current_temp) else (False, error)
        """
        if not is_valid_temperature_unit(unit):
            return False, 'Invalid temperature unit.'

        if not is_valid_lat_lon(lat, lon):
            return False, 'Invalid latitude and/or longitude.'

        ret, data = post_request(self.url, json_data={'lat': float(lat), 'lon': float(lon)})
        if not ret:
            return False, data

        current_temp = data.get('query').get('results').get('channel').get('condition').get('temp')
        return True, current_temp
