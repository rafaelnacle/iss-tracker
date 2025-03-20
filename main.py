import requests
from datetime import datetime

# Cianorte - Paraná location
MY_LAT = -23.6633
MY_LNG = -52.6055
TIME_ZONE = -3
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # My position is within +5 or -5 degrees of the iss position
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True

def is_night_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + TIME_ZONE
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + TIME_ZONE

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

is_iss_overhead()

