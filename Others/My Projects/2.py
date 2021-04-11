import smtplib
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("aritra.mukhopadhyay@niser.ac.in", "dyjxzm22UH")
server.sendmail("aritra.mukhopadhyay@niser.ac.in", "swayam.panda@niser.ac.in", "This is a Python generated mail")
