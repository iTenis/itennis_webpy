#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from __future__ import unicode_literals
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import traceback

def send_exception_email(title,exc):
    mail_info = {
        "from": "itennishy@qq.com",
        "to": "563376097@qq.com",
        "hostname": "smtp.qq.com",
        "username": "itennishy@qq.com",
        "password": "bwrabwxkbgbccigi",
        "mail_subject": title,
        "mail_text": '',
        "mail_encoding": "ascii"
    }
    smtp = SMTP_SSL(mail_info["hostname"])
    smtp.set_debuglevel(1)
    smtp.ehlo(mail_info["hostname"])  # 提示使用认证
    smtp.login(mail_info["username"], mail_info["password"])
    mail_msg = exc
    msg = MIMEMultipart('related')
    msgAlternative = MIMEMultipart('alternative')
    msg.attach(msgAlternative)
    msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
    msg["Subject"] = Header(mail_info["mail_subject"], "utf-8")
    msg["from"] = mail_info["from"]
    msg["to"] = mail_info["to"]
    smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())
    smtp.quit()


def decorator_error_monitor(title):
    def wrap(f):
        def wrapped_f(*args,**kwargs):
            try:
                result = f(*args,**kwargs)
                return result
            except:
                exc = traceback.format_exc()
                send_exception_email(title,exc)
                raise Exception(exc)
        return wrapped_f
    return wrap