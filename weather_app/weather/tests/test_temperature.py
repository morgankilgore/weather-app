from unittest import mock, TestCase
from weather.utils import temperature


class TestGetAverageTemp(TestCase):
    @mock.patch('weather.utils.temperature.is_valid_temperature_value', autospec=True)
    def test_valid_temperatures(self, mock_is_valid_temperature_value):
        params = {
            'temps': [30, -2.5, 0, 100.5],
            'avg_temp_response': (True, 32),
            'mock_is_valid_temperature_value_return': True
        }
        mock_is_valid_temperature_value.return_value = params.get('mock_is_valid_temperature_value_return')

        resp = temperature.get_average_temp(params.get('temps'))
        self.assertEqual(resp, params.get('avg_temp_response'))

    @mock.patch('weather.utils.temperature.is_valid_temperature_value', autospec=True)
    def test_invalid_temperatures(self, mock_is_valid_temperature_value):
        params = {
            'temps': [30, -2.5, 0, 100.5],
            'avg_temp_response': (False, 'Invalid temperature value'),
            'mock_is_valid_temperature_value_return': False
        }
        mock_is_valid_temperature_value.return_value = params.get('mock_is_valid_temperature_value_return')

        resp = temperature.get_average_temp(params.get('temps'))
        self.assertEqual(resp, params.get('avg_temp_response'))
