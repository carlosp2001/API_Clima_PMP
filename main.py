# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import json

url="https://api.openweathermap.org/data/2.5/weather"
params={"q":"Tegucigalpa","appid":"63aed104a1fc299178c8eed99f65fd6f"}
response=requests.get(url, params=params)
jsonDataString=response.text
jsonDictionary=json.loads(jsonDataString)
temperaturamax=round((int(jsonDictionary["main"]["temp_max"]))-273.15,2)
temperaturamin=round((int(jsonDictionary["main"]["temp_min"]))-273.15,2)
temperatura=round(int((jsonDictionary["main"]["temp"]))-273.15,2)
ciudad=jsonDictionary["name"]
print("La temperatura actual en ",ciudad," es", str(temperatura)," °C")
print("Se espera una temperatura maxima de ",str(temperaturamax)," °C")
print("Y una temperatura minima de ",str(temperaturamin)," °C")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
