import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'First Last'
email['to'] = 'email@email.com'
email['subject'] = 'Test email sender with Python language'

email.set_content('testing email')

with smtplib.SMTP(host='smtp.office365.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email@email.com', 'password')
    smtp.send_message(email)
    print('all done! ')