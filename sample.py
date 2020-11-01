# coding: utf-8

from config import MAIL_ADDRESS, PASSWORD, TO_MAIL_ADDRESS
from email.mime.text import MIMEText
from email.utils import formatdate

import smtplib
smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.ehlo()
print(smtpobj.login(MAIL_ADDRESS, PASSWORD))

body_msg = "本日10時より、俯瞰システムソフトウェア開発の業務を開始いたします。よろしくお願いいたします。"
subject = "11月1日就労報告：開始（宮本望）"
msg = MIMEText(body_msg)
msg['Subject'] = subject
msg['From'] = MAIL_ADDRESS
msg['To'] = TO_MAIL_ADDRESS
msg['Date'] = formatdate()
print(msg)