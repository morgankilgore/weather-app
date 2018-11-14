from unittest import mock
from django.test import TestCase
from weather.weather_provider.weather_dot_com import WeatherDotCom


class GetCurrentTempTest(TestCase):

    @mock.patch('weather.weather_provider.weather_dot_com.is_valid_temperature_unit')
    @mock.patch('weather.weather_provider.weather_dot_com.is_valid_lat_lon')
    @mock.patch('weather.weather_provider.weather_dot_com.post_request')
    def test_success(self, mock_post_request, mock_is_valid_lat_lon, mock_is_valid_temperature_unit):
        mock_is_valid_lat_lon.return_value = True
        mock_is_valid_temperature_unit.return_value = True
        mock_post_request.return_value = True, {'query': {'results': {'channel': {'condition': {'temp': 20}}}}}

        weather_dot_com = WeatherDotCom()
        ret, resp = weather_dot_com.get_current_temp(20, 100)

        self.assertEqual(True, ret)
        self.assertEqual(20, resp)

    @mock.patch('weather.weather_provider.weather_dot_com.is_valid_temperature_unit')
    def test_invalid_temperature_unit(self, mock_is_valid_temperature_unit):
        mock_is_valid_temperature_unit.return_value = False

        weather_dot_com = WeatherDotCom()
        ret, resp = weather_dot_com.get_current_temp(20, 100)

        self.assertEqual(False, ret)
        self.assertEqual('Invalid temperature unit.', resp)

    @mock.patch('weather.weather_provider.weather_dot_com.is_valid_temperature_unit')
    @mock.patch('weather.weather_provider.weather_dot_com.is_valid_lat_lon')
    def test_invalid_lat_lon(self, mock_is_valid_lat_lon, mock_is_valid_temperature_unit):
        mock_is_valid_lat_lon.return_value = False
        mock_is_valid_temperature_unit.return_value = True

        weather_dot_com = WeatherDotCom()
        ret, resp = weather_dot_com.get_current_temp(20, 100)

        self.assertEqual(False, ret)
        self.assertEqual('Invalid latitude and/or longitude.', resp)

    @mock.patch('weather.weather_provider.weather_dot_com.is_valid_temperature_unit')
    @mock.patch('weather.weather_provider.weather_dot_com.is_valid_lat_lon')
    @mock.patch('weather.weather_provider.weather_dot_com.post_request')
    def test_post_request_error(self, mock_post_request, mock_is_valid_lat_lon, mock_is_valid_temperature_unit):
        mock_is_valid_lat_lon.return_value = True
        mock_is_valid_temperature_unit.return_value = True
        mock_post_request.return_value = False, 'Post request error'

        weather_dot_com = WeatherDotCom()
        ret, resp = weather_dot_com.get_current_temp(20, 100)

        self.assertEqual(False, ret)
        self.assertEqual('Post request error', resp)
