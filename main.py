from email.message import EmailMessage as EM
import ssl, os, smtplib, imghdr

number_of_recipients = 2
email_sender = 'youremail@gmail.com'
email_pass = os.environ.get("EMAIL_PASS")
email_receiver, names = [], []

print('Enter the email addresses of receiver :')
for i in range(number_of_recipients): email_receiver.append(input())
print('\nEnter the names of receiver :')
for i in range(number_of_recipients): names.append(input())

subject = 'New Py Tutorial'
em = EM()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject

for nickname, receiver in zip(names, email_receiver):
    body = 'Hello ' + nickname + '''
you can access the new python tutorial through the link :
https://www.youtube.com/watch?v=g_j6ILT-X0k
    '''
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_pass)
        smtp.sendmail(email_sender, receiver, em.as_string())