import requests
import random
import pandas as pd
from citipy import citipy

def fetch_raw_data(api_key):
    url = "http://api.openweathermap.org/data/2.5/weather?"

#This will fetch raw data from the API