import requests
from datetime import datetime

# Cianorte - Paraná location
MY_LAT = -23.6633
MY_LNG = -52.6055
TIME_ZONE = -3

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}



response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise_utc = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_utc = data["results"]["sunset"].split("T")[1].split(":")[0]
sunrise_time = datetime.strptime(sunrise_utc, "%H").hour + TIME_ZONE
sunset_time = datetime.strptime(sunset_utc, "%H").hour + TIME_ZONE


time_now = datetime.now()


