import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendmessagetomail():
	host = "smtp.gmail.com:587"
	server=smtplib.SMTP(host)
	sender="automailpython@gmail.com"
	recipient=["ssasirekha95@gmail.com"]
	msg=MIMEMultipart()
	msg['Subject']="automailpython test mail" 
	msg['From']=sender
	msg['To'] = ",".join(recipient)
	#multiple recipients ["a@ma.com",b@ma.com]
	#can do html formating in mimetext
	msg.attach(MIMEText("This is the test message"))
	
	print("processing mail")
	try:
		server.sendmail(sender, recipient, msg.as_string())
		print("sent mail")
	except smtplib.SMTPException:
		print("Error:Unable to send e-mail")
	server.quit()
	print("message processed")

sendmessagetomail()



