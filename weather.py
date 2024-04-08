import requests
from dotenv import load_dotenv
import os

load_dotenv
api_key=os.getenv('API_KEY')

def get_lang_long(city_name, state_code, country_code, API_key):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
   
    data = response[0]
    lat, lon =data.get('lat'), data.get('lon')
    return lat, lon

    #print(response)

#get_lang_long('Dublin','Dublin','Ireland', api_key)

print(get_lang_long('Dublin','Leinster', 'Ireland', api_key))        
