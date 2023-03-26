import datetime
import requests
import urllib.request
import json
import sys

key = "fa024d2a350b4df484c42502232603"

def get_ip():
    api_url = "https://ipinfo.io/json"
    print("requesting ip")
    response = requests.get(api_url)
    print("done requesting ip")
    ip = response.json()["ip"].split(",")
    return str(ip[0])

ip = get_ip()

now = datetime.datetime.now()
days = []
days.append(str(now.replace(hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(days=1))[:11])
days.append(str(now.replace(hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(days=2))[:11])
days.append(str(now.replace(hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(days=3))[:11])
days.append(str(now.replace(hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(days=4))[:11])
days.append(str(now.replace(hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(days=5))[:11])
print(ip)
built_api_url = "http://api.weatherapi.com/v1/history.json?key=fa024d2a350b4df484c42502232603 &q=" + ip + "&dt="
temp_mins =[]
temp_maxs = []
count = 0
for day in days:
    print("requesting")
    response = requests.get(built_api_url+day)
    print("received")
    j = response.json()
    min = j["forecast"]["forecastday"][0]["day"]["mintemp_f"]
    temp_mins.append(min)
    max = j["forecast"]["forecastday"][0]["day"]["maxtemp_f"]
    temp_maxs.append(max)
    count += 1

print(temp_mins, temp_maxs)


