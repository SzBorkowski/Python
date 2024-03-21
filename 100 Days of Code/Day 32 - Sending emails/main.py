import smtplib
import datetime as dt
from threading import Timer
import random

my_email = "pythn688@gmail.com"
password = "pesw wsfa ydmm pols"

# SENDING EMAILS
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="simon345@wp.pl",
#                         msg="Subject:Hello!\n\nEmail body")
#
#
# DATETIME PRACTICE
# now = dt.datetime.now()
# year = now.year
# print(year)
#
# date_of_birth = dt.datetime(year=1997, month=7, day=6)
# print(date_of_birth)
#
#
# SENDING A QUOTE ON MONDAYS
# with open("quotes.txt") as f:
#     data = f.readlines()
#     quote = random.choice(data)
#
#
# def send_quote():
#     print("Sending a quote")
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email,
#                             to_addrs="simon345@wp.pl",
#                             msg=f"Subject:Motivational quote for today\n\n{quote}")
#
# while True:
#     now = dt.datetime.now()
#     if now.weekday() == 3:
#         send_quote()
#         # Call your CODE() function here
#         break
#
#
# SENDING BIRTHDAY WISHES AUTOMATICALLY
#
# def send_wishes():
#     print("Sending wishes")
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email,
#                             to_addrs="simon345@wp.pl",
#                             msg="Subject:It's your birthday!\n\nHappy birthday!")
#
# while True:
#     now = dt.datetime.now()
#     if now.hour==18 and now.minute==35 and now.second==30:
#         send_wishes()
#         # Call your CODE() function here
#         break
#
