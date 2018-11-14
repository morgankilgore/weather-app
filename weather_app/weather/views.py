from weather.weather_provider.noaa import Noaa
from weather.weather_provider.weather_dot_com import WeatherDotCom
from weather.weather_provider.accu_weather import AccuWeather
from weather.utils.temperature import get_average_temp
from weather.utils.response import create_json_response
from weather.utils.validation import is_valid_filters


def avg_temp(request):
    """
    Returns average temperature from requested filters

    Param(s):
        latitude (float): Required. Latitude of location
        longitude (float): Requried. Longitude of location
        filter (str): Requred. Weather service to query

    Returns json. {'status': 'success', 'avg_temp': <avg_temp>} on success, else {'status': 'error', 'error': <error_msg>}
    """
    if request.method == 'GET':
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        filters = request.GET.getlist('filter')

        if not latitude or not longitude or not filters:
            return create_json_response({'error': 'User should provide latitiude, longitude, and filters with request'}, status_code=400)

        if not is_valid_filters(filters):
            return create_json_response({'error': 'User supplied invalid filters.'}, status_code=400)

        current_temps = []
        for provider in filters:
            if provider == 'noaa':
                noaa = Noaa()
                ret, data = noaa.get_current_temp(latitude, longitude)
                if not ret:
                    return create_json_response({'error': data}, status_code=400)
                current_temps.append(data)
            elif provider == 'weather.com':
                weatherdotcom = WeatherDotCom()
                ret, data = weatherdotcom.get_current_temp(latitude, longitude)
                if not ret:
                    return create_json_response({'error': data}, status_code=400)
                current_temps.append(data)
            elif provider == 'accuweather':
                accuweather = AccuWeather()
                ret, data = accuweather.get_current_temp(latitude, longitude)
                if not ret:
                    return create_json_response({'error': data}, status_code=400)
                current_temps.append(data)

        ret, data = get_average_temp(current_temps)
        if not ret:
            return create_json_response({'error': data}, status_code=400)
        return create_json_response({'avg_temp': data}, status_code=200)
    else:
        return create_json_response({'error': 'Invalid request method'}, status_code=400)
