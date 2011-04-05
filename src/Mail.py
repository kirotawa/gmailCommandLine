

import os
import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.Utils import formatdate
from email import Encoders


class Mail(object):
	
	
	def __init__(self, **paramms):
		self.fromaddr = paramms['user_email']
		self.passwd = paramms['passwd']
		self.toaddrs = paramms['dest']
		self.subject = paramms['sub']
		self.content = paramms['msg'] 
		self.attach = paramms['attach']
		self.email = self.load()

		if self.attach is not None:
			self.attaching()

	def load(self):
		msg = MIMEMultipart()
		msg['From'] = self.fromaddr
		msg['To'] = self.toaddrs
		msg['Subject'] = self.subject	
		msg['Date'] = formatdate(localtime = True)
		msg.attach(MIMEText(self.content, 'plain'))
		return msg
	
	def attaching(self):
		try:
			filepath = r'%s' % self.attach			
			attach_part = MIMEBase('application', "octet-stream")
			attach_part.set_payload(open(filepath,"rb").read())
			Encoders.encode_base64(attach_part)
			attach_part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(filepath))
			self.email.attach(attach_part)
		except:				
			print "Filed on attach file. Verify if the path of file was given and try again. Report error to kirotaw[here goes a sign]gmail[here a dot]com."
		

	def send(self):
		try:
			server = smtplib.SMTP('smtp.gmail.com:587')
			server.starttls()
			server.login(self.fromaddr,self.passwd)
			server.sendmail(self.fromaddr, self.toaddrs, self.email.as_string())
			server.quit()
		except:
			print "Filed on send email. Verify if was are given all datas. Report error to kirotawa[hereve goes a sign]gmail[here a dot]com"
