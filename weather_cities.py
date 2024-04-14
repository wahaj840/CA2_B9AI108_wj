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


#As we will be analysing data of different cities of Ireland so i have defined the latitude and longitude for Ireland baseed on which we will be pulling the data from the website Via API

# Latitude limits for Ireland
lat_min= 51.5
lat_max=55.5

# Longitude limits for Ireland
lon_min= -11.5
lon_max=-6








