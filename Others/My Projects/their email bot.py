import smtplib
import email.message
from pprint import pprint

def send_email(recipient, subject, message):
    smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login("code@niser.ac.in", "")
    msg = email.message.Message()
    msg["From"] = "Coding Club"
    msg["To"] = recipient
    msg["Subject"] = "Welcome to Coding Club!"
    msg["Content-Type"] = "text/html"
    msg.set_payload( "<font size=4 face='monospace'>{}</font>".format(message))
    smtpObj.sendmail("Coding Club", recipient, msg.as_string())
    smtpObj.quit()

fin = open("kids.csv")
ids = {}
for line in fin:
    info = line.strip("\n").split(",")
    mail = info[0]
    name = info[1]
    ids[name] = mail

for kid in ids:
    print("{}, {}".format(ids[kid], kid.split()[0]))
    send_email(ids[kid], "Welcome to Coding Club!",
"""Welcome to the Coding Club.<br>
Here are the details for your first briefing:<br><br>
<strong>Venue</strong>: <a href="https://meet.google.com/wnx-ssph-cag">wnx-ssph-cag</a><br>
<strong>Date</strong>: 01 January 2021 (today)<br>
<strong>Time</strong>: 2200 hours<br><br>
See you there, {}.
<br><br>
~Coding Club""".format(kid.split()[0]))
