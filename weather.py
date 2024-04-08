import requests
from dotenv import load_dotenv
import os

load_dotenv
api_key=os.getenv('API_KEY')

def get_lang_long(city_name, state_code, country_code, API_key):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}')

    print(response)

get_lang_long('Houston','Texas', 'United States', api_key)
        
