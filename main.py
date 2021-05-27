# Simple Mail Transfer Protocal
import smtplib
from email.message import EmailMessage
from cred import sender_email, sender_password

msg = EmailMessage()

msg["Subject"] = input("Enter a subject:\n")
msg["From"] = sender_email
msg["To"] = sender_email
msg.set_content(input("Enter a message:\n"))

sender_email = sender_email
sender_password = sender_password

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(sender_email, sender_password)
server.send_message(msg)
server.quit()

print("Message Successfully Sent!")