# -*- coding: utf-8 -*-

"""Copyright (C) 2011 by Leonidas S. Barbosa  - kirotawa@gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE."""

import os
import smtplib
from email import Encoders
from email.Utils import formatdate
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

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
			attach_part.add_header('Content-Disposition', 'attachment; filename=\
                                    "%s"' % os.path.basename(filepath))
			self.email.attach(attach_part)
		except:				
			print "Failed on attach file. Verify if the path of file was given \
            and try again. Report error to kirotawa[here goes a sign]gmail[here \
            a dot]com."
		

	def send(self):
		try:
			server = smtplib.SMTP('smtp.gmail.com:587')
			server.starttls()
			server.login(self.fromaddr,self.passwd)
			server.sendmail(self.fromaddr, self.toaddrs, self.email.as_string())
			server.quit()
			print "Successfully sent email!"
		except smtplib.SMTPException:
			print "ERROR"	
