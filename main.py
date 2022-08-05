from re import sub
import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
smtp_object.starttls()

email = input('Input your email: ')
password = getpass.getpass(prompt='Input Gmail PIN ' )
smtp_object.login(email,password)

emailBody = open('emailContents/emailBody.txt')
emailBody = emailBody.read()

emailSubject = open('emailContents/emailSubject.txt')
emailSubject = emailSubject.read()

from_address = email
to_address = input('Input their email: ')
subject = emailSubject
message = emailBody
msg = "Subject: "+subject+'\n'+message

smtp_object.sendmail(from_address,to_address,msg)
