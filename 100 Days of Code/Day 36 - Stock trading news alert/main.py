import os
import requests
from datetime import date
from datetime import timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

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

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yerstday's closing stock price.
response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMS)
response.raise_for_status()
data = response.json()

today = date.today()
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
    global article1, article2, article3
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"{article1}\n{article2}\n{article3}",
        from_="+12055493689",
        to=verified_phone
    )
    print(message.status)


ystday_price = data["Time Series (Daily)"][f"{yesterday}"]["4. close"]
b4ystday_price = data["Time Series (Daily)"][f"{b4yesterday}"]["4. close"]
price_diff = float(ystday_price) - float(b4ystday_price)
if price_diff < 0:
    price_diff *= -1
trigger = float(ystday_price) * 0.05
if price_diff > trigger:
    print("Get News")
    get_news()
    send_sms()
get_news()
send_sms()

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
# HINT 1: Think about using the Python Slice Operator


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
# HINT 1: Consider using a List Comprehension.
account_sid = "ACb65f258128faaea33e133366265f11a4"
auth_token = os.environ['TWILIO_AUTH_TOKEN']
verified_phone = os.environ['TWILIO_VERIFIED_PHONE']

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
