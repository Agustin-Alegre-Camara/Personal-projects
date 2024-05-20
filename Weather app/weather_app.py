import requests
import os
from datetime import datetime, timedelta

api_key = 'bafc2506ebf850f112d2fc75ad92def8'

print('Welcome to the wheater app forecast')
location = input('Entyer the name of the city:')
complete_api_link = 'https://api.openweathermap.org/data/2.5/weather?q='+location+'&appid='+str(api_key)

api_link = requests.get(complete_api_link)
api_data = api_link.json()
print(api_data)

if api_data['cod'] == '404':
    print('Sorry, it seems {0} is not in our database yet. Please try another city.')
else:
    city_temp = ((api_data["main"]["temp"]) - 273.15)
    temp_like = ((api_data['main']['feels_like']) - 273.15)
    weather_description = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_speed = api_data['wind']['speed']
    date_and_time = datetime.now().strftime('%d %b %Y | %H:%M')

print(30 * '-')
print('Weather stats for {0} | {1}'.format(location.upper(), date_and_time))
print(30 * '-')
print('''
#Temperature (ºC) : {0:.0f}
#Feels like  (ºC) : {1:.0f}
#Weather          : {2}
#Wind speed (Km/h): {3}
#Humidity (%)     : {4}
'''.format(city_temp, temp_like, weather_description, wind_speed, hmdt))
