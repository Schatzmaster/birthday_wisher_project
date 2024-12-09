# --------------------Modules------------------
import datetime as dt
import random
import pandas as pd
import smtplib

# --------------------SMTPLIB------------------
EMAIL = "_YOUR_EMAIL_"
PASSWORD = "_YOUR_PASSWORD"

# --------------------Datetime------------------
now = dt.datetime.now()
today = (now.day, now.month)

# --------------------Pandas------------------
data = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row["day"], data_row["month"]): data_row for (index, data_row) in data.iterrows()}

# --------------------Code------------------

if today in birthday_dict:
    b_day_letter = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(b_day_letter) as letter:
        content = letter.read()
        content = content.replace("[NAME]", birthday_dict[today]["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="jasp.hanson@gmail.com",
                            msg=f"Subject:Happy Birthday\n\n {content}")


