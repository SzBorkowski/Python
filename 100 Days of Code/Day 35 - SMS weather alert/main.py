import os
import requests
from twilio.rest import Client

# https://api.openweathermap.org/data/2.5/weather?lat=52.229675&lon=21.012230&appid=f5b7565e36039b5af8bf5edb254b87e1

OMW_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ['OMW_API_KEY']
account_sid = "ACb65f258128faaea33e133366265f11a4"
auth_token = os.environ['TWILIO_AUTH_TOKEN']
verified_phone = os.environ['TWILIO_VERIFIED_PHONE']
params = {
    "lat": 52.229675,
    "lon": 21.012230,
    "appid": api_key,
    "cnt": 4,
}

# Getting forecast from Open Weather
response = requests.get(url=OMW_endpoint, params=params)
response.raise_for_status()
weather_data = response.json()

# Checking for rainy weather
will_rain = False
for forecast in range(params["cnt"]):
    if weather_data["list"][forecast]["weather"][0]["id"] < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_="+12055493689",
        to=verified_phone
    )
    print(message.status)
