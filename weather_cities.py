import requests
import random
from datetime import datetime
import csv
import pandas as pd
import matplotlib.pyplot as plt

import sys                                 # This package will output the nearest city to a specific pair of geographical  coordinates. It is very important for this project.
import citipy
from citipy import citipy


#Defining the URL where we will be fetching the data, its units and the API key
url="http://api.openweathermap.org/data/2.5/weather?"
units ='metric'
api_key="c542897b543bb199a66f36f6de4e89c5"


#As we will be analysing data of different cities of Ireland and UK so i have defined the latitude and longitude for Ireland baseed on which we will be pulling the data from the website Via API

# Latitude limits for Ireland & UK
lat_min= 50
lat_max=60

# Longitude limits for Ireland & UK
lon_min= -10.5
lon_max= 2

# Setting a counter and create an empty list for holding the city and country information
counter=0
cities=[]

#Generating random lat and lon cordinates within IRE and UK
#iterations set to 50
while counter< 50:
    lat=random.uniform(lat_min,lat_max)
    lon=random.uniform(lon_min,lon_max)

    #Finding the nearest city to the assigned cordinates
    city=citipy.nearest_city(lat,lon).city_name

    #Check wheather city is not already existing
    if city not in cities:
        cities.append(city)
        counter +=1

   # API call code (URL where we will be fetching the data, its units and the API key)
query_url= f"{url}appid={api_key}&units={units}&q="
units='metric'
api_key='c542897b543bb199a66f36f6de4e89c5'














