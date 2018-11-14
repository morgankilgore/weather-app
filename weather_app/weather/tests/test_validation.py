from unittest import TestCase
from weather.utils import validation


class TestIsValidTemperatureUnit(TestCase):
    def test_valid_temperature_unit(self):
        units = ['Fahrenheit', 'fahrenheit', 'celsius', 'Celsius']

        for unit in units:
            self.assertEqual(True, validation.is_valid_temperature_unit(unit))

    def test_invalid_temperature_unit(self):
        units = ['Invalid', 'invalid', '', ' ']

        for unit in units:
            self.assertEqual(False, validation.is_valid_temperature_unit(unit))


class TestIsValidLatLon(TestCase):
    def test_valid_lat_lon(self):
        lat_lon_list = [(10, 1.2), (-4, -2.3), ('3', '-23.4')]

        for lat, lon in lat_lon_list:
            self.assertEqual(True, validation.is_valid_lat_lon(lat, lon))

    def test_invalid_lat_lon(self):
        lat_lon_list = [('test', 1.2), ('-4', 'test-2.3')]

        for lat, lon in lat_lon_list:
            self.assertEqual(False, validation.is_valid_lat_lon(lat, lon))


class TestIsValidTemperatureValue(TestCase):
    def test_valid_temperature_value(self):
        temps = ['-23.4', 12.4, '3', 0, -2]

        for temp in temps:
            self.assertEqual(True, validation.is_valid_temperature_value(temp))

    def test_invalid_temperature_value(self):
        temps = ['test', 'invalid-13']

        for temp in temps:
            self.assertEqual(False, validation.is_valid_temperature_value(temp))
