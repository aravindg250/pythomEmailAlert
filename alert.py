import smtplib
from email.message import EmailMessage
import time
import json
import os

f = open('config.json')
data = json.load(f)

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["to"] = to
    msg["from"] = "Name of User"
    #Name of User is the name of the sender that you want to display

    user = data["email"] #Data from config.json
    password = data["password"] #Data from config.json


    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(user, password)
    server.send_message(msg)
    server.quit()
    f.close()
    
for i in range(10): #Change 1 to the number of emails you want to recieve
    if __name__ == "__main__":
        email_alert("Subject of Email", "Body Of Email", "Email of Receiver")
        time.sleep(0) #Number of seconds after each email.


#Verizon
#<10-digit-number>@vtext.com

#T-Mobile/Mint
#<10-digit-number>@tmomail.net

#AT&T
#<10-digit-number>@txt.att.net

#Sprint
#<10-digit-number>@messaging.sprintpcs.com


