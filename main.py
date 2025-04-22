import smtplib as smtp
from email.mime import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config

sender_email = config.sender_mail
sender_password = config.sender_password
receiver = config.receiver_mail

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver
msg["Subject"] = "This is the test text subject"
body = "This is the body of the test test. "

try:
    s = smtp.SMTP('smtp.gmail.com', 587)
    msg.attach(MIMEText(body,"plain"))
    s.starttls()
    s.login(sender_email,sender_password)
    s.sendmail(sender_email,receiver,msg.as_string())
    print("Email Sent")
except Exception as e :
    print("Email Not Sent")
finally:
    s.quit()






