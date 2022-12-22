import os
# connect to mail server
import smtplib
from email.message import EmailMessage

# Using credentials from my environment variables
EMAIL_ADDRESS = os.environ.get('GMAIL_USER')  # 'w.rosales40@gmail.com'
EMAIL_PASSWORD = os.environ.get('GMAIL_PASS')  # 'nybthlsdowceqtsy'

# Create message
msg = EmailMessage()
msg['Subject'] = 'Dinner'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS
msg.set_content('Hey want to go to dinner at 7pm?')

# Log in to gmail servers using credentials and send message.
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login to Gmail server
    smtp.send_message(msg)
