from datetime import datetime

import requests

from TranasctionWeather.settings import MAP_BOX_KEY, WEATHER_KEY


def weather(address):
    map_address = address.replace(' ', '%20')
    map_call = f'https://api.mapbox.com/geocoding/v5/mapbox.places/{map_address}.json?types=address&access_token={MAP_BOX_KEY}'
    coordinates_data = requests.get(map_call).json()
    lon = coordinates_data['features'][0]['center'][0]
    lat = coordinates_data['features'][0]['center'][1]
    weather_call = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&exclude=alerts,minutely&appid={WEATHER_KEY}'
    one_call = requests.get(weather_call).json()
    forecast_date = datetime.fromtimestamp(one_call['current']['dt']).strftime('%A, %d %B %Y %H:%M')
    feels_like = one_call['current']['feels_like']
    next_parse = one_call['daily']
    daily_data = {}
    for next_p in next_parse:
        daily_data[datetime.fromtimestamp(next_p['dt']).strftime('%A, %d %B %Y %H:%M')] = {
            'max_temp': next_p['temp']['max'],
            'min_temp': next_p['temp']['min'],
            'description': next_p['weather'][0]['description'],
        }
    hourly_data = {}
    second_parse = one_call['hourly']
    for sec in second_parse:
        hourly_data[datetime.fromtimestamp(sec['dt']).strftime('%A, %d %B %Y %H:%M')] = sec['feels_like']
    return {'date': forecast_date, 'feels': feels_like, 'hour': hourly_data, 'daily': daily_data}