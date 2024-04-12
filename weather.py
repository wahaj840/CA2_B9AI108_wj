import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass
import csv
import pandas as pd

load_dotenv
api_key=os.getenv('API_KEY')

@dataclass
class WeatherData:
    main:str
    description: str
    icon: str
    tempreture: float
    min_tempreture: float
    max_tempreture: float
    air_pressure: int
    humidity: int
    visibility: int
    wind_speed: float
    wind_degree: int
    


def get_lang_long(city_name, state_code, country_code, API_key):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
   
    data = response[0]
    lat, lon =data.get('lat'), data.get('lon')
    return lat, lon

    #print(response)


# Fetching and saving the Unprocessed data in a CSV

def fetch_raw_data(city_name, state_name, country_name):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}')

    if response.status.code ==200:
        raw_data=response.json
        return raw_data
    else:
        print("Failed to Fetch the data")
        return None


city_name="Dublin"
state_name="Leinster"
country_name="Ireland"    

raw_data= fetch_raw_data(city_name, state_name, country_name)




#get_lang_long('Dublin','Leinster','Ireland', api_key)


def get_current_weather(lat, lon, API_key):
    response= requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
   
    data= WeatherData(
        main=response.get('weather')[0].get('main'),
        description=response.get('weather')[0].get('description'),
        icon=response.get('weather')[0].get('icon'),
        tempreture=response.get('main').get('temp'),
        min_tempreture=response.get('main').get('temp_min'),
        max_tempreture=response.get('main').get('temp_max'),
        air_pressure=response.get('main').get('pressure'),
        humidity=response.get('main').get('humidity'),
        visibility=response.get('visibility'),
        wind_speed=response.get('wind').get('speed'),
        wind_degree=response.get('wind').get('deg'),
        )
    
    return data


def main (city_name, state_name, country_name):
    lat,lon = get_lang_long('Dublin','Leinster', 'Ireland', api_key)
    weather_data= get_current_weather(lat, lon, api_key)
    return weather_data
    


if __name__=="__main__":
    lat ,lon = get_lang_long('Dublin','Leinster', 'Ireland', api_key)

    print(get_current_weather(lat, lon, api_key))



#print(get_lang_long('Dublin','Leinster', 'Ireland', api_key))    











#Fetching and saving the processed data in a CSV

data = get_current_weather(53.349805, -6.26031, api_key)



df = pd.DataFrame({
    'Main': [data.main],
    'Description': [data.description],
    'Icon': [data.icon],
    'Temperature': [data.tempreture],
    'Min Temperature': [data.min_tempreture],
    'Max Temperature': [data.max_tempreture],
    'Air Pressure': [data.air_pressure],
    'Humidity': [data.humidity],
    'Visibility': [data.visibility],
    'Wind Speed': [data.wind_speed],
    'Wind Degree': [data.wind_degree]
})

csv_file="weather_data1.csv"

df.to_csv(csv_file, index=False)

    
print (" Processed Weather Data has been stored in csv file successfully. File Name:" ,csv_file)