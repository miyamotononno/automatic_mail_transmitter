# coding: utf-8
from email.utils import formatdate
from config import NAME, WORK_CONTENTS
from mail import MyMail
from datetime import date

if '__file__' in globals():
  import os, sys
  sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

if __name__ == "__main__":
  body_msg = u"本日の業務を14時にて終了いたします。よろしくお願いいたします。"
  subject = u"{0}月{1}日就労報告：終了（{2}）".format(date.today().month,date.today().day, NAME)
  m = MyMail()
  m.create_mail(body_msg, subject)
  m.send_mail()