import requests

API = "5ef5daebcc1fd3f969ebbec99c99e0f2"
base_url = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a City Name:")
request_url = f"{base_url}?appid={API}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp']-273.15, 2)
    print("Weather:", weather)
    print("Temperature", temperature, "C")
else:
    print("An Error Occured.")