from re import sub
import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
smtp_object.starttls()

email = 'oconnorabram@gmail.com'
password = 'pqawwemqnzoitapm'
smtp_object.login(email,password)

from_address = email
to_address = email
subject = input('Body.txt')
message = input('Input message here: ')
msg = "Subject: "+subject+'\n'+message

smtp_object.sendmail(from_address,to_address,msg)