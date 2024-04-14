import requests
import random
import pandas as pd
from citipy import citipy

def fetch_raw_data(api_key):
    url = "http://api.openweathermap.org/data/2.5/weather?"
    units ='metric'
    api_key="c542897b543bb199a66f36f6de4e89c5"


'''Copying code from weather_cities file'''
# Latitude limits for Ireland & UK  
lat_min= 50
lat_max=60

# Longitude limits for Ireland & UK
lon_min= -10.5
lon_max= 2

# Setting a counter and create an empty list for holding the city and country information
counter=0
cities=[]

while counter<50:   #Generating random lat and lon cordinates w.r.t the assigned range
    lat =random.uniform(lat_min, lat_max)
    lon=random.unform(lon_min, lon_max)
    city = citipy.nearest_city(lat, lon).city_name
    if city not in cities:
     cities.append(city)
     counter+=1

