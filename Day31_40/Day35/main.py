import requests
import os
from twilio.rest import Client

account_sid = os.environ.get("ACCOUNT_SID_KEY")
auth_token = os.environ.get("AUTH_TOKEN_KEY")
my_fone = os.environ.get("MY_PHONE_KEY")
twilio_virtual_phone = os.environ.get("TWILIO_VIRTUAL_PHONE_KEY")

API_KEY = os.environ.get("OWM_API_KEY")
ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "lat":-21.162778,
    "lon":-47.849979,
    "cnt":4,
    "appid": API_KEY
}

response = requests.get(url=ENDPOINT, params=weather_params)
response.raise_for_status()

weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Vai chover hoje! Lembre-se de levar um guarda-chuva.☂️",
        from_=twilio_virtual_phone,
        to=my_fone
    )
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Hoje não chove. Fique tranquilo.☀️",
        from_=twilio_virtual_phone,
        to=my_fone
    )

print(message.status)