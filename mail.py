# coding: utf-8

from config import MAIL_ADDRESS, PASSWORD, TO_MAIL_ADDRESS
from email.mime.text import MIMEText
from email.utils import formatdate
import datetime
import smtplib

class MyMail:
  def __init__(self):
    self.mail_address = MAIL_ADDRESS
    self.password = PASSWORD
    self.to_mail_address = TO_MAIL_ADDRESS
    self.msg = None

  def create_mail(self, body_msg, subject):
    msg = MIMEText(body_msg)
    msg['Subject'] = subject
    msg['From'] = self.mail_address
    msg['To'] = self.to_mail_address
    msg['Date'] = formatdate(localtime=True)
    print(msg)
    self.msg = msg

  def _create_log(self, error=True):
    d_today = datetime.date.today()
    dt_now = datetime.datetime.now()

    fileName = "logs/{0}/{1}.txt".format(d_today, dt_now.hour)
    file = open(fileName, "w")
    if error:
      file.write('error!')
    else:
      file.write('success!')
    file.close()
  
  def send_mail(self):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    try:
      smtpobj.ehlo()
      smtpobj.starttls()
      smtpobj.ehlo()
      smtpobj.login(self.mail_address, self.password)
      smtpobj.sendmail(self.mail_address, self.to_mail_address, self.msg.as_string())
      smtpobj.close()
    except smtplib.SMTPException as e:
      print('error happened! cannot send email')
      self._create_log()