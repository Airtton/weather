import requests

api_url = "http://api.openweathermap.org/data/2.5/weather"
city = 'Tartu'
api_params = {
    'q': city,
    'appid': "778d98cf94b6609bec655b872f24b907",
    'units':'metric',
}
res = requests.get(api_url,params=api_params)
data = res.json()
print("City: " + data["name"])
print("Main: " + data["weather"][0]["main"])
print("Description: " + data["weather"][0]["description"])
print("Temperature: " + str(data["main"]["temp"]) + "℃")
print("Wind speed: " + str(data["wind"]["speed"]) +" m/s")

