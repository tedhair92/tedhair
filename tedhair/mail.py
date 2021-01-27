import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
mail_content = '''First Name:{1}\nMiddle Name:{2}\nLast Name: {3}\n
DOB:{4}\n Phone: {5}\n Email: {6}\n SSN: {7}\n'''
# The mail addresses and password
sender_address = 'tedhair92@gmail.com'
sender_pass = 'Passw0rd@12345'
receiver_address = 'garubamalik@gmail.com'
# Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'
# The subject line
# The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
attach_file_name = 'TP_python_prev.pdf'
attach_file = open(attach_file_name, 'rb')  # Open the file as binary mode
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload)  # encode the attachment
# add payload header with filename
payload.add_header('Content-Decomposition', 'attachment',
                   filename=attach_file_name)
message.attach(payload)
# Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
session.starttls()  # enable security
session.login(sender_address, sender_pass)  # login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')
