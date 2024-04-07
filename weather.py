import requests

def get_lang_long(city_name, state_code, country_code, limit, API_key):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={API_key}')
    