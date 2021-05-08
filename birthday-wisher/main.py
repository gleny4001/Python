# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)


import smtplib
from datetime import datetime
import pandas
import random

my_email = "gleny4001@gmail.com"
password = "1234"
today = (datetime.now().month, datetime.now().day)

# pandas
data = pandas.read_csv("birthdays.csv")
new_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today in new_dict:
    birthday_person = new_dict[today]
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        # Create smtp object
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Transport Layer security - secures the email (Encryption)
            connection.starttls()
            # login to the email
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="gleny4001@gmail.com",
                                msg=f"Subject:Happy birthday!! \n\n {contents}")
