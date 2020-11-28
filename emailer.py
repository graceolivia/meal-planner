import smtplib,ssl
from email.mime.text import MIMEText
from config import *
print(sender)
print(sendee)
print(password)
message = "hoi"
port = 465
context = ssl.create_default_context()


#get the meals
with open('text/history.txt', 'r') as history:
    message = history.read()
    history.close()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, sendee, message)
