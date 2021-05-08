import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

account_sid = os.environ.get("API_KEY")
auth_token = os.environ.get("AUTH_TOKEN")
appid =  os.environ.get("APPID")

weather_params = {
    "lat": "37.491885",
    "lon": "126.487989",
    "appid": appid,
    "exclude": "current,minutely,daily"
}


response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
response.raise_for_status()
data = response.json()["hourly"]

will_rain = False
for i in range(0, 12):
    if data[i]["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token)
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It will rain! Bring an umbrella",
        from_='+12162086557',
        to='+821074526787'
    )