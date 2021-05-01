import requests
from datetime import datetime
MY_LAT = 13.415180
MY_LNG = -11.831497


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])
time_now = datetime.now()
print(time_now.hour)