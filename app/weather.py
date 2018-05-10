import json
import requests
from app import app

def getWeather(zip):
    if 'OPENWEATHER_API_KEY' not in app.config or \
            not app.config['OPENWEATHER_API_KEY']:
        return ('Error: the weather service is not configured.')

    api_url = 'http://api.openweathermap.org/data/2.5/weather'
    appid = ...    
    r = requests.get(url=api_url, params=dict(q=zip,units='imperial', APPID= app.config['OPENWEATHER_API_KEY']))
    if r.status_code != 200:
        return (r.status_code)
    return r.json()