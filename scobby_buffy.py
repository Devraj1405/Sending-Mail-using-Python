#This code is for sending an email through gmail from one account to another via python code
#Before you start sending ccode, you may need to enable POP and IMAP from your gmail settings. Also Make sure you turn on
#the Allow less secure apps, for accessing and sending mails.

import smtplib

host = "smtp.gmail.com"
port = 587
username = "enter_your_email_here@gmail.com"
password = "enter_your_email_password_here"

from_email = username
to_list = ["enter_the_person's_email_to_whom_you_want_to_send_the_mail@gmail.com"]

email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()  								#This will show the message indicating that google is ready wo work with you
email_conn.starttls()							#This is basically for encryption purpoeses
email_conn.login(username, password)
email_conn.sendmail(from_email, to_list, "Hello there this is an email message")
email_conn.quit()


#This is another method for sending mails, here I have added a while loop. 
#On changing the value of i you can send as many mails u want continuosly.

from smtplib import SMTP
i=0
while i<5:
	ABC = SMTP(host, port)
	ABC.ehlo()
	ABC.starttls()
	ABC.login(username, password)
	ABC.sendmail(from_email, to_list, "Hello this is number {0}".format(i))
	ABC.quit()
	i+=1

from smtplib import SMTP, SMTPAuthenticationError, SMTPException


pass_wrong = SMTP(host, port)
pass_wrong.ehlo()
pass_wrong.starttls()
try:
    pass_wrong.login(username, "wrong_password")
    pass_wrong.sendmail(from_email, to_list, "Hello there this is an email message")
except SMTPAuthenticationError:
    print("Could not login")
except:
    print("an error occured")

pass_wrong.quit()

#Don't start using this for spamming others. It's fun, but don't.