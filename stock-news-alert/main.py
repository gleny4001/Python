import requests
import os
import datetime as dt
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import random

STOCK = "NKLA"
COMPANY_NAME = "Nikola Inc"

stock_api_key = os.environ.get("STOCK_API_KEY")
news_api_key = os.environ.get("NEWS_API_KEY")

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

stock_param = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": stock_api_key,
}

news_param = {
    "q": COMPANY_NAME,
    "apikey": news_api_key
}
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# --------------------------------------Stock price-------------------------------------------------#
year = dt.datetime.now().year
month = dt.datetime.now().month
yesterday = dt.datetime.today() - dt.timedelta(2)
yesterday = dt.datetime.strftime(yesterday, '%Y-%m-%d')

day_before_yesterday = dt.datetime.today() - dt.timedelta(3)
day_before_yesterday = dt.datetime.strftime(day_before_yesterday, '%Y-%m-%d')

# Stock data
stock_response = requests.get(STOCK_ENDPOINT, params=stock_param)
stock_response.raise_for_status()
stock_data = stock_response.json()['Time Series (60min)']

yesterday_high = float(stock_data[f"{yesterday} 16:00:00"]['4. close'])
day_before_yesterday_high = float(stock_data[f"{day_before_yesterday} 16:00:00"]['4. close'])

dif = yesterday_high - day_before_yesterday_high

# ----------------------------------------News------------------------------------------------------#

news_response = requests.get(NEWS_ENDPOINT, params=news_param)
news_response.raise_for_status()
news_data = news_response.json()['articles'][:3]

news_to_send = news_data[random.randint(0, len(news_data) - 1)]

# ------------------------------------------SMS---------------------------------------------------#
if 100 * abs(dif) / day_before_yesterday_high > 0:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token)
    # client = Client(account_sid, auth_token, http_client=proxy_client)
    if dif < 0:
        up_down = f"NKLA: {round(dif,2)}%"
    elif dif > 0:
        up_down = f"NKLA: {round(dif,2)}%"

    message = client.messages \
        .create(
        body=f"\n{up_down}\n\n Headline: {news_to_send['title']}\n\n Brief: {news_to_send['description']}",
        from_='+12162086557',
        to='+821074526787'
    )
    print(message.status)
