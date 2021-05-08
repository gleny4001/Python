import smtplib
import datetime as dt
import random

my_email = "gleny4001@gmail.com"
password = "1234"
now = dt.datetime.now()

if now.weekday() == 0:
    with open("quotes.txt") as quote_file:
        lines = quote_file.readlines()
        random.shuffle(lines)
        Quote_of_the_day = lines[random.randint(0, len(lines) - 1)]

    # Create smtp object
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Transport Layer security - secures the email (Encryption)
        connection.starttls()
        # login to the email
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="gleny4001@gmail.com",
                            msg=f"Subject:Quote of the day \n\n{Quote_of_the_day}")
