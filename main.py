from email.message import EmailMessage
from email.policy import SMTP
import os
import ssl
import smtplib

email_sender = 'youremail@gmail.com'
email_pass = os.environ.get("EMAIL_PASS")

email_receiver = []
number_of_recipients = 5
for i in range(number_of_recipients): email_receiver.append(input())

subject = 'New Py Tutorial'
body = '''
you can access the new tutorial through the link :
https://www.youtube.com/watch?v=g_j6ILT-X0k
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_pass)
    smtp.sendmail(email_sender, email_receiver, em.as_string())