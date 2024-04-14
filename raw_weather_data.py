import requests
import random
import pandas as pd
from citipy import citipy

url = "http://api.openweathermap.org/data/2.5/weather?"
units = 'metric'
api_key = "c542897b543bb199a66f36f6de4e89c5"

def fetch_raw_weather_data():
    lat_min = 50
    lat_max = 60
    lon_min = -10.5
    lon_max = 2
    cities = []
    counter = 0
    while counter < 50:
        lat = random.uniform(lat_min, lat_max)
        lon = random.uniform(lon_min, lon_max)
        city = citipy.nearest_city(lat, lon).city_name
        if city not in cities:
            cities.append(city)
            counter += 1
    weather_data = []
    for city in cities:
        try:
            response = requests.get(f"{url}appid={api_key}&units={units}&q={city}").json()
            weather_data.append(response)
        except Exception as e:
            print(f"Error occurred for {city}: {e}")
    return weather_data

