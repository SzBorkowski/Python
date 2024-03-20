# import smtplib
#
# my_email = "pythn688@gmail.com"
# password = "pesw wsfa ydmm pols"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="simon345@wp.pl",
#                         msg="Subject:Hello!\n\nEmail body")
#
import datetime as dt

now = dt.datetime.now()
year = now.year
print(year)

date_of_birth = dt.datetime(year=1997, month=7, day=6)
print(date_of_birth)
