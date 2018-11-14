import requests
from unittest import mock
from django.test import TestCase
from weather.utils import request


class GetRequestTest(TestCase):
    @mock.patch('weather.utils.request.requests', autospec=True)
    def test_success(self, mock_requests):
        mock_requests_get_return_value = {'unit': 'test'}

        with mock.patch.object(mock_requests, 'get') as mock_requests_get:
            mock_requests_get.return_value.json = mock.PropertyMock(return_value=mock_requests_get_return_value)
            ret, resp = request.get_request('unit-test.com')

            self.assertEqual(ret, True)
            self.assertEqual(resp, mock_requests_get_return_value)

    @mock.patch('weather.utils.request.requests', autospec=True)
    def test_connection_error(self, mock_requests):
        mock_requests.exceptions = requests.exceptions

        with mock.patch.object(mock_requests, 'get') as mock_requests_get:
            mock_requests_get.side_effect = requests.exceptions.ConnectionError
            ret, resp = request.get_request('unit-test.com')

            self.assertEqual(ret, False)
            self.assertEqual(resp, 'Error in connecting to unit-test.com')


class PostRequestTest(TestCase):
    @mock.patch('weather.utils.request.requests', autospec=True)
    def test_success(self, mock_requests):
        mock_requests_post_return_value = {'unit': 'test'}

        with mock.patch.object(mock_requests, 'post') as mock_requests_post:
            mock_requests_post.return_value.json = mock.PropertyMock(return_value=mock_requests_post_return_value)
            ret, resp = request.post_request('unit-test.com')

            self.assertEqual(ret, True)
            self.assertEqual(resp, mock_requests_post_return_value)

    @mock.patch('weather.utils.request.requests', autospec=True)
    def test_connection_error(self, mock_requests):
        mock_requests.exceptions = requests.exceptions

        with mock.patch.object(mock_requests, 'post') as mock_requests_post:
            mock_requests_post.side_effect = requests.exceptions.ConnectionError
            ret, resp = request.post_request('unit-test.com')

            self.assertEqual(ret, False)
            self.assertEqual(resp, 'Error in connecting to unit-test.com')
