import requests
from ui import WeatherInterface
from data_bank import Data_Bank
import json
import os


## Function to call API and Store data in JSON 
def make_api_call():
    data = requests.get(url=path_latest_data , params=weather_params)
    data.raise_for_status()
    data_json = data.json()
    with open("latest_weather_data.json" , "w") as file:
        json.dump(data_json, file, indent=4)




#Here I get access to the data via API and 
path_latest_data = "https://api.openweathermap.org/data/2.5/weather"
weather_params = {
    "lat": "",
    "lon": "",
    "appid": "",
    "units": "metric" # to get temperature in celcius and wind in m/s
}

## Make API Call and store data in json
make_api_call()

# ## Load Data from json File 
with open("latest_weather_data.json" , "r") as file:

    latest_data = json.load(file)

print(type(latest_data))
print(latest_data["weather"])


## Call Function which saves the data to the data bank 
data_store = Data_Bank(latest_data)
data_store.show_db()
old_data = data_store.get_old_data(data_store.is_new_db)


 

## Call the Weather Interface 
interface = WeatherInterface(latest_data, old_data, data_store.is_new_db)



