import requests
from datetime import datetime
import smtplib
import time
import os
from dotenv import load_dotenv

load_dotenv()
MY_EMAIL = os.getenv("MY_EMAIL_KEY")
MY_PASSWORD = os.getenv("MY_PASSWORD_KEY")

MY_LAT = -21.163485 # Your latitude
MY_LONG = -47.833306 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    time_now = int(time_now)

    if time_now >= sunrise or time_now <= sunset:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            to_addrs=MY_EMAIL,
            from_addr=MY_EMAIL,
            msg="Subject:ISS Overhead!\n\nLook up the ISS is passing by you! ☝️"
        )


