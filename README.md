# weather-app
Django app that calls a mock weather api to return data

## Requirements
The following environment variables need to be set:
- `SECRET_KEY`: Django secret key
- `WEATHER_API_URL`: URL to the mock weather api

## Setup
```
# Create virtualenv
mkvirtualenv weather-app
# Activate virtualenv
workon weather-app
# Install required packages
pip install -r requirements.txt
# Run django development server
cd weather_app
python manage.py runserver
```

## Routes
**Host:** http://127.0.0.1:8000/weather

#### Average temperature
**URL:** /avg-temp
**HTTP Method:** GET
**Params:** 
- latitude: *Required.* Latitude of location
- longitude: *Required.* Longitude of location
- filter: *Required.* Which weather service to get data from. Currently supported: 'weather.com', 'noaa', 'accuweather'. To query more than one weather service, add additional filter parameters.


## Example
Get average temp from weather.com
`curl http://127.0.0.1:8000/weather/avg-temp?latitude=234&longitude=123&filter=weather.com`

Get the average temperature from weather.com and noaa
`curl http://127.0.0.1:8000/weather/avg-temp?latitude=234&longitude=123&filter=weather.com&filter=noaa`
