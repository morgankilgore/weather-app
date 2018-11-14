from unittest import mock
from django.test import TestCase
from weather.weather_provider.accu_weather import AccuWeather


class GetCurrentTempTest(TestCase):

    @mock.patch('weather.weather_provider.accu_weather.is_valid_temperature_unit')
    @mock.patch('weather.weather_provider.accu_weather.is_valid_lat_lon')
    @mock.patch('weather.weather_provider.accu_weather.get_request')
    def test_success(self, mock_get_request, mock_is_valid_lat_lon, mock_is_valid_temperature_unit):
        mock_is_valid_lat_lon.return_value = True
        mock_is_valid_temperature_unit.return_value = True
        mock_get_request.return_value = True, {'simpleforecast': {'forecastday': [{'current': {'fahrenheit': 20}}]}}

        accu_weather = AccuWeather()
        ret, resp = accu_weather.get_current_temp(20, 100)

        self.assertEqual(True, ret)
        self.assertEqual(20, resp)

    @mock.patch('weather.weather_provider.accu_weather.is_valid_temperature_unit')
    def test_invalid_temperature_unit(self, mock_is_valid_temperature_unit):
        mock_is_valid_temperature_unit.return_value = False

        accu_weather = AccuWeather()
        ret, resp = accu_weather.get_current_temp(20, 100)

        self.assertEqual(False, ret)
        self.assertEqual('Invalid temperature unit.', resp)

    @mock.patch('weather.weather_provider.accu_weather.is_valid_temperature_unit')
    @mock.patch('weather.weather_provider.accu_weather.is_valid_lat_lon')
    def test_invalid_lat_lon(self, mock_is_valid_lat_lon, mock_is_valid_temperature_unit):
        mock_is_valid_lat_lon.return_value = False
        mock_is_valid_temperature_unit.return_value = True

        accu_weather = AccuWeather()
        ret, resp = accu_weather.get_current_temp(20, 100)

        self.assertEqual(False, ret)
        self.assertEqual('Invalid latitude and/or longitude.', resp)

    @mock.patch('weather.weather_provider.accu_weather.is_valid_temperature_unit')
    @mock.patch('weather.weather_provider.accu_weather.is_valid_lat_lon')
    @mock.patch('weather.weather_provider.accu_weather.get_request')
    def test_get_request_error(self, mock_get_request, mock_is_valid_lat_lon, mock_is_valid_temperature_unit):
        mock_is_valid_lat_lon.return_value = True
        mock_is_valid_temperature_unit.return_value = True
        mock_get_request.return_value = False, 'Get request error'

        accu_weather = AccuWeather()
        ret, resp = accu_weather.get_current_temp(20, 100)

        self.assertEqual(False, ret)
        self.assertEqual('Get request error', resp)
