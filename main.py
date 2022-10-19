#Monday Motivation Project
import smtplib
import datetime as dt
import random

MY_EMAIL = "appbreweryinfo@gmail.com"
MY_PASSWORD = "abcd1234()"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:   # SMTP host is different for different email provider
        connection.starttls()   # Secure (encrypt) the email - Transport Layer Security
        connection.login(MY_EMAIL, MY_PASSWORD)   # Sender email login
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )