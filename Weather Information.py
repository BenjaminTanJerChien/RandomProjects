#weather information

import requests
from pprint import pprint
import json


api_key = "5574c1bfb4db55a7afaa32379ff6f35b"
city = input("City name: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + api_key + "&q=" + city

weather_data = requests.get(base_url).json()

city = weather_data["name"]
desc = weather_data["weather"][0]["description"]

print(f"The weather in {city} is {desc}")
