import requests
from datetime import datetime
import smtplib

MY_LAT = 37.491953  # Your latitude
MY_LONG = 37.491953  # Your longitude
my_email = "gleny4001@gmail.com"
password = "1a2s3d4F5G-"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
def iss_is_up():
    if abs(iss_latitude - MY_LAT) < 6 and abs(iss_longitude - MY_LONG) < 6:
        return True


def is_dark():
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

    time_now = datetime.now()
    if sunset <= time_now.hour <= sunrise:
        return True


if iss_is_up() and is_dark():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Transport Layer security - secures the email (Encryption)
        connection.starttls()
        # login to the email
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:Look up! \n\n ISS is on the sky!!")
