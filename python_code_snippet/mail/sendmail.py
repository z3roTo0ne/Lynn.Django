# # coding=utf-8
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# sender = 'chenlin_youdao@126.com'
# receiver = '412369794@qq.com'
# subject = '邮件发送测试'
# smtpserver = 'smtp.126.com'
# username = 'chenlin_youdao'
# password = ''
#
# msg = MIMEText('邮件发送测试', 'plain', 'utf-8')
# msg['Subject'] = Header(subject, 'utf-8')
#
# # from 和 to这两个不能少
# msg['from'] = sender
# msg['to'] = receiver
# smtp = smtplib.SMTP()
# smtp.connect('smtp.126.com')
# smtp.login(username, password)
# smtp.sendmail(sender, receiver, msg.as_string())
# smtp.quit()
#
#


# from smtplib import SMTP_SSL
# from email.header import Header
# from email.mime.text import MIMEText
#
# mail_info = {
#     "from": "412369794@qq.com",
#     "to": "412369794@qq.com",
#     "hostname": "smtp.qq.com",
#     "username": "412369794",
#     "password": "pxnqsrihmiibbghh",
#     "mail_subject": "test",
#     "mail_text": "hello, this is a test email, sended by py",
#     "mail_encoding": "utf-8"
# }
#
# if __name__ == '__main__':
#     # 这里使用SMTP_SSL就是默认使用465端口
#     smtp = SMTP_SSL(mail_info["hostname"])
#     smtp.set_debuglevel(1)
#
#     smtp.ehlo(mail_info["hostname"])
#     smtp.login(mail_info["username"], mail_info["password"])
#
#     msg = MIMEText(mail_info["mail_text"], "plain", mail_info["mail_encoding"])
#     msg["Subject"] = Header(mail_info["mail_subject"], mail_info["mail_encoding"])
#     msg["from"] = mail_info["from"]
#     msg["to"] = mail_info["to"]
#
#     smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())
#
#     smtp.quit()



# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'report@camera360.com'
receiver = 'chenlin@camera360.com'
subject = '邮件发送测试'
smtpserver = 'smtp.exmail.qq.com'
username = 'report@camera360.com'
password = '9Pf5A&k$f2wX1'

msg = MIMEText('邮件发送测试', 'plain', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')

# from 和 to这两个不能少
msg['from'] = sender
msg['to'] = receiver
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
