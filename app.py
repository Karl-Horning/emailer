import smtplib
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import Config

# Get the emails from the files
with open('email.html','r') as html_file:
    email_body_html = BeautifulSoup(html_file, "html.parser")

with open("email.txt") as text_file:
    email_body_text = text_file.read()

# Set up the sender, receiver, and username and password for the email
email_from = Config.EMAIL_ADDRESS
email_to = Config.EMAIL_RECIPIENT
username = Config.USERNAME
password = Config.PASSWORD

# Build the main elements of the email
email = MIMEMultipart('alternative')
email['From'] = email_from
email['To'] = email_to
email['Subject'] = 'Test Email'
email.attach(MIMEText(email_body_text, 'plain'))
email.attach(MIMEText(email_body_html, 'html'))

# Send the email
# Google
# server = smtplib.SMTP('smtp.gmail.com:587')
# Outlook
server = smtplib.SMTP('smtp-mail.outlook.com:25')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.sendmail(email_from, email_to, email.as_string())
server.quit()

print(f'Email sent from {email_from} to {email_to}.')