import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 52.229675
MY_LONG = 21.012230
TIMEZONE = "Europe/Warsaw"
my_email = "pythn688@gmail.com"
password = "pesw wsfa ydmm pols"
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": TIMEZONE,
}


def check_pos():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(f"Checking on ISS. Current position: {iss_latitude, iss_longitude}")
    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT + 5 >= iss_latitude >= MY_LAT + 5 and MY_LONG + 5 >= iss_longitude >= MY_LONG + 5:
        return True


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour


def check_time():
    if sunrise >= int(time_now) or sunset <= int(time_now):
        return True


# If the ISS is close to my current position
# and it is currently dark
while True:
    if check_pos() and check_time():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg="Subject:Look up!\n\nThere's an ISS passing by!")
            print("Email sent!")
    time.sleep(5)
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
