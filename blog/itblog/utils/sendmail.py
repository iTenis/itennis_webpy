#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from __future__ import unicode_literals
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import traceback

def send_email(tomail,context):
    mail_info = {
        "from": "itennishy@qq.com",
        "to": tomail,
        "hostname": "smtp.qq.com",
        "username": "itennishy@qq.com",
        "password": "bwrabwxkbgbccigi",
        "mail_subject": 'iTennis验证系统',
        "mail_text": context,
        "mail_encoding": "ascii"
    }
    smtp = SMTP_SSL(mail_info["hostname"])
    smtp.set_debuglevel(1)
    smtp.ehlo(mail_info["hostname"])  # 提示使用认证
    smtp.login(mail_info["username"], mail_info["password"])
    mail_msg = "<p>iTennis柠檬-密码验证</p><p>验证码:<a href=\"http://www.itennishy.com\">"+mail_info["mail_text"]+"</a></p>"
    msg = MIMEMultipart('related')
    msgAlternative = MIMEMultipart('alternative')
    msg.attach(msgAlternative)
    msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
    msg["Subject"] = Header(mail_info["mail_subject"], "utf-8")
    msg["from"] = mail_info["from"]
    msg["to"] = mail_info["to"]
    smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())
    smtp.quit()
