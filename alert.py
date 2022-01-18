import smtplib
from email.message import EmailMessage

import json
import os

f = open('config.json')
data = json.load(f)

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["to"] = to
    msg["from"] = "Name of Sender"
    #Name of User is the name of the sender that you want to display

    user = data["email"]
    password = data["password"]


    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(user, password)
    server.send_message(msg)
    server.quit()
    f.close()
for i in range(10):
    if __name__ == "__main__":
        email_alert("Subject of Email", "Body of Email", "Email of Reciever")


#Verizon
#<10-digit-number>@vtext.com

#T-Mobile
#<10-digit-number>@tmomail.com

#AT&T
#<10-digit-number>@txt.att.net

#Sprint
#<10-digit-number>@messaging.sprintpcs.com


