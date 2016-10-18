import requests

data = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=94720,us&APPID=1c45f1223de502c389919db8eee5774e")

json = data.json()

print(json['name'])