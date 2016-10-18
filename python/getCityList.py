import requests

data = requests.get("http://api.openweathermap.org/data/2.5/weather?id=5327684&APPID=1c45f1223de502c389919db8eee5774e")

json = data.json()

print("city: {0} | ID: {1}".format(json['name'], json['id']))
print(json['sys']['sunrise'])