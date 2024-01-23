import requests

api_key = '91a709ebda96b152133fd14fc1c58661'
city = input('Enter city name: ')
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

print(url)
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    #print(f'Temperature: {temp} K')
    print(f'Temperature: {temp} °C')
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')

    