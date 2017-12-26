#In the previous code we sent a simple text mail, here I have added the code part for adding a subject and also
#how to add the HTML code to customize your text message.

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib

host = "smtp.gmail.com"
port = 587
username = "enter_your_email_here@gmail.com"
password = "enter_your_email_password_here"

from_email = username
to_list = ["enter_the_person's_email_to_whom_you_want_to_send_the_mail@gmail.com"]


try:
	email_conn = smtplib.SMTP(host, port)
	email_conn.ehlo()  								#This will show the message indicating that google is ready wo work with you
	email_conn.starttls()							#This is basically for encryption purpoeses
	email_conn.login(username, password)
	the_msg = MIMEMUltipart("alternative")
	the_msg['subject'] = "Hello there!"
	the_msg["From"] = from_email

	plain_txt = "This is a text meassage"
	html_txt = """\
	<html>
		<body>
			<b>
				<p>This is<br>a message<br>with line breaks</p>
			</b>
		</body>	
	</html>
	"""
	part_1	= MIMEText(plain_txt, 'plain')
	part_2 = MIMEText(html_txt, "html")
	the_msg.attach(part_1)
	the_msg.attach(part_2)
	email_conn.sendmail(from_email, to_list, the_msg.as_string())
	email_conn.quit()
except smtplib.SMTPException:
	print ("Error sending mail")

