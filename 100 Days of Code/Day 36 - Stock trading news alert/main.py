import os
import requests
from datetime import date, timedelta, datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
TREND = "🔺"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_KEY = "4ZE2OHP2NTWBMLRX"
STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_KEY,
}
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY = "93c55fa22e3647fd87a8403991f18775"
NEWS_PARAMS = {
    "apiKey": NEWS_KEY,
    "q": "Tesla",
}
account_sid = "ACb65f258128faaea33e133366265f11a4"
auth_token = os.environ['TWILIO_AUTH_TOKEN']
verified_phone = os.environ['TWILIO_VERIFIED_PHONE']


# Getting info about stock price movement
response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMS)
response.raise_for_status()
data = response.json()

# Setting the dates for today, yesterday
today = date.today()
today_weekday = today.weekday()
while True:
    if today_weekday > 5:
        today -= timedelta(days=1)
        today_weekday = today.weekday()
    else:
        break
yesterday = today - timedelta(days=1)
b4yesterday = today - timedelta(days=2)


def get_news():
    global article1, article2, article3
    response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMS)
    response.raise_for_status()
    data = response.json()
    article1 = data["articles"][0]["title"]
    article2 = data["articles"][1]["title"]
    article3 = data["articles"][2]["title"]


def send_sms():
    global article1, article2, article3, percentage_diff
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"{STOCK}: {TREND}{int(percentage_diff)}%\n{article1}\n{article2}\n{article3}",
        from_="+12055493689",
        to=verified_phone
    )
    print(message.status)


# Main code, checking price movements and sending SMS if it's more than 5%
ystday_price = data["Time Series (Daily)"][f"{yesterday}"]["4. close"]
b4ystday_price = data["Time Series (Daily)"][f"{b4yesterday}"]["4. close"]
price_diff = float(ystday_price) - float(b4ystday_price)
if price_diff < 0:
    TREND = "🔻"
    price_diff *= -1
percentage_diff = price_diff / float(ystday_price) * 100
trigger = float(ystday_price) * 0.05
if price_diff > trigger:
    print("Get News")
    get_news()
    send_sms()
