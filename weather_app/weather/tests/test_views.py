from unittest import mock
from django.test import TestCase


class AvgTempViewTest(TestCase):

    @mock.patch('weather.views.Noaa', autospec=True)
    @mock.patch('weather.views.is_valid_filters', autospec=True)
    @mock.patch('weather.views.get_average_temp', autospec=True)
    def test_success(self, mock_get_average_temp, mock_is_valid_filters, mock_noaa):
        params = {
            'query_values': {'latitude': 10, 'longitude': 11, 'filter': 'noaa'},
            'mock_current_temp_return': [True, 30],
            'mock_is_valid_filters_return': True,
            'mock_get_average_temp_return': [True, 30],
            'api_return': {'status': 'success', 'status_code': 200, 'avg_temp': 30}
        }

        noaa_instance = mock_noaa.return_value
        noaa_instance.get_current_temp.return_value = params.get('mock_current_temp_return')
        mock_is_valid_filters.return_value = params.get('mock_is_valid_filters_return')
        mock_get_average_temp.return_value = params.get('mock_get_average_temp_return')

        result = self.client.get('/weather/avg-temp', params.get('query_values'))
        self.assertEqual(result.status_code, params.get('api_return').get('status_code'))
        self.assertEqual(result.json().get('status'), params.get('api_return').get('status'))
        self.assertEqual(result.json().get('avg_temp'), params.get('api_return').get('avg_temp'))

    @mock.patch('weather.views.is_valid_filters', autospec=True)
    def test_invalid_filters(self, mock_is_valid_filters):
        params = {
            'query_values': {'latitude': 10, 'longitude': 11, 'filter': 'noaa'},
            'mock_is_valid_filters_return': False,
            'api_return': {'status': 'error', 'status_code': 400, 'error': 'User supplied invalid filters.'}
        }

        mock_is_valid_filters.return_value = params.get('mock_is_valid_filters_return')

        result = self.client.get('/weather/avg-temp', params.get('query_values'))
        self.assertEqual(params.get('api_return').get('status_code'), result.status_code)
        self.assertEqual(params.get('api_return').get('status'), result.json().get('status'))
        self.assertEqual(params.get('api_return').get('error'), result.json().get('error'))

    def test_incomplete_query_values(self):

        params = {
            'query_values': [
                {},
                {'latitude': 10},
                {'longitude': 11},
                {'filter': 'noaa'},
                {'latitude': 10, 'longitude': 11},
                {'latitude': 10, 'filter': 'noaa'},
                {'longitude': 11, 'filter': 'noaa'}
            ],
            'mock_is_valid_filters_return': False,
            'api_return': {'status': 'error', 'status_code': 400, 'error': 'User should provide latitiude, longitude, and filters with request'}
        }

        for query_value in params.get('query_values'):
            result = self.client.get('/weather/avg-temp', query_value)
            self.assertEqual(params.get('api_return').get('status_code'), result.status_code)
            self.assertEqual(params.get('api_return').get('status'), result.json().get('status'))
            self.assertEqual(params.get('api_return').get('error'), result.json().get('error'))

    @mock.patch('weather.views.Noaa', autospec=True)
    @mock.patch('weather.views.is_valid_filters', autospec=True)
    def test_error_from_noaa_get_current_temp(self, mock_is_valid_filters, mock_noaa):
        params = {
            'query_values': {'latitude': 10, 'longitude': 11, 'filter': 'noaa'},
            'mock_current_temp_return': [False, 'Dummy error'],
            'mock_is_valid_filters_return': True,
            'api_return': {'status': 'error', 'status_code': 400, 'error': 'Dummy error'}
        }

        noaa_instance = mock_noaa.return_value
        noaa_instance.get_current_temp.return_value = params.get('mock_current_temp_return')
        mock_is_valid_filters.return_value = params.get('mock_is_valid_filters_return')

        result = self.client.get('/weather/avg-temp', params.get('query_values'))
        self.assertEqual(result.status_code, params.get('api_return').get('status_code'))
        self.assertEqual(result.json().get('status'), params.get('api_return').get('status'))
        self.assertEqual(result.json().get('error'), params.get('api_return').get('error'))

    @mock.patch('weather.views.WeatherDotCom', autospec=True)
    @mock.patch('weather.views.is_valid_filters', autospec=True)
    def test_error_from_weather_dot_com_get_current_temp(self, mock_is_valid_filters, mock_weather_dot_com):
        params = {
            'query_values': {'latitude': 10, 'longitude': 11, 'filter': 'weather.com'},
            'mock_current_temp_return': [False, 'Dummy error'],
            'mock_is_valid_filters_return': True,
            'api_return': {'status': 'error', 'status_code': 400, 'error': 'Dummy error'}
        }

        weather_dot_com_instance = mock_weather_dot_com.return_value
        weather_dot_com_instance.get_current_temp.return_value = params.get('mock_current_temp_return')
        mock_is_valid_filters.return_value = params.get('mock_is_valid_filters_return')

        result = self.client.get('/weather/avg-temp', params.get('query_values'))
        self.assertEqual(result.status_code, params.get('api_return').get('status_code'))
        self.assertEqual(result.json().get('status'), params.get('api_return').get('status'))
        self.assertEqual(result.json().get('error'), params.get('api_return').get('error'))

    @mock.patch('weather.views.AccuWeather', autospec=True)
    @mock.patch('weather.views.is_valid_filters', autospec=True)
    def test_error_from_accu_weather_get_current_temp(self, mock_is_valid_filters, mock_accu_weather):
        params = {
            'query_values': {'latitude': 10, 'longitude': 11, 'filter': 'accuweather'},
            'mock_current_temp_return': [False, 'Dummy error'],
            'mock_is_valid_filters_return': True,
            'api_return': {'status': 'error', 'status_code': 400, 'error': 'Dummy error'}
        }

        accu_weather_instance = mock_accu_weather.return_value
        accu_weather_instance.get_current_temp.return_value = params.get('mock_current_temp_return')
        mock_is_valid_filters.return_value = params.get('mock_is_valid_filters_return')

        result = self.client.get('/weather/avg-temp', params.get('query_values'))
        self.assertEqual(result.status_code, params.get('api_return').get('status_code'))
        self.assertEqual(result.json().get('status'), params.get('api_return').get('status'))
        self.assertEqual(result.json().get('error'), params.get('api_return').get('error'))

    @mock.patch('weather.views.Noaa', autospec=True)
    @mock.patch('weather.views.is_valid_filters', autospec=True)
    @mock.patch('weather.views.get_average_temp', autospec=True)
    def test_error_from_get_average_temp(self, mock_get_average_temp, mock_is_valid_filters, mock_noaa):
        params = {
            'query_values': {'latitude': 10, 'longitude': 11, 'filter': 'noaa'},
            'mock_current_temp_return': [True, 30],
            'mock_get_average_temp_return': [False, 'Dummy error'],
            'mock_is_valid_filters_return': True,
            'api_return': {'status': 'error', 'status_code': 400, 'error': 'Dummy error'}
        }

        noaa_instance = mock_noaa.return_value
        noaa_instance.get_current_temp.return_value = params.get('mock_current_temp_return')
        mock_is_valid_filters.return_value = params.get('mock_is_valid_filters_return')
        mock_get_average_temp.return_value = params.get('mock_get_average_temp_return')

        result = self.client.get('/weather/avg-temp', params.get('query_values'))
        self.assertEqual(result.status_code, params.get('api_return').get('status_code'))
        self.assertEqual(result.json().get('status'), params.get('api_return').get('status'))
        self.assertEqual(result.json().get('error'), params.get('api_return').get('error'))

    def test_invalid_request_method(self):
        params = {
            'api_return': {'status': 'error', 'status_code': 400, 'error': 'Invalid request method'}
        }

        result = self.client.put('/weather/avg-temp')
        self.assertEqual(result.status_code, params.get('api_return').get('status_code'))
        self.assertEqual(result.json().get('status'), params.get('api_return').get('status'))
        self.assertEqual(result.json().get('error'), params.get('api_return').get('error'))
