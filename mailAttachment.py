import os
import smtplib
import imghdr
from email.message import EmailMessage

# Using credentials from my environment variables
EMAIL_ADDRESS = os.environ.get('GMAIL_USER')  # my email
EMAIL_PASSWORD = os.environ.get('GMAIL_PASS')  # my email password

# Contact list
contacts = [EMAIL_ADDRESS]  # Could add more contacts

# Create email message
msg = EmailMessage()
msg['Subject'] = 'Check out these files!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts
msg.set_content('So funny right?')

# Lists of files to send
imageFiles = ['/home/wilber/Downloads/catFace.jpg', '/home/wilber/Downloads/dogMeme.jpg']
pdfFiles = ['/home/wilber/Downloads/humorLaws.pdf']

# Go through image list, so each file can be read and attached.
for file in imageFiles:
    with open(file, 'rb') as f:
        fileData = f.read()
        fileType = imghdr.what(f.name)
        fileName = f.name

    msg.add_attachment(fileData, maintype='image', subtype=fileType, filename=fileName)

# Go through pdf list, so each file can be read and attached.
for file in pdfFiles:
    with open(file, 'rb') as f:
        fileData = f.read()
        fileName = f.name

    msg.add_attachment(fileData, maintype='application', subtype='octet-stream', filename=fileName)

# Log in to gmail servers using credentials and send message.
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
