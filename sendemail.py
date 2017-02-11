import smtplib

from_addr = 'taje.carter@gmail.com'
to_addr  = 'david@someemail.com'
from_name = 'Taje Carter'
to_name = 'David'
subject = 'Test Mail'
message = """
From: {} <{}>
To: {} <{}>
Subject: {}
{}
"""
message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, message)
# Credentials (if needed)
username = 'username@gmail.com'
password = 'password'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit()