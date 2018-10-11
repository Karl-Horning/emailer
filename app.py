import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import Config

email_from = Config.EMAIL_ADDRESS
email_to = Config.EMAIL_RECIPIENT
email_body = 'Hello, World!'
username = Config.USERNAME
password = Config.PASSWORD

email = MIMEMultipart()
email['From'] = email_from
email['To'] = email_to
email['Subject'] = 'Test Email'
email.attach(MIMEText(email_body))

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
