# from email import encoders
# from email.header import Header
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email.utils import parseaddr,formataddr

# import smtplib

# def _formate_addr(s):
#     name,addr = parseaddr(s)
#     return formataddr((Header(name,'utf-8').encode(),addr))

# from_addr = '240272750@qq.com'
# password = 'eoywmleeedikbjjj'
# to_addr = '13387565008@163.com'
# smtp_server = 'smtp.qq.com'
# #发送纯文本邮件
# # msg = MIMEText('hello,send by python...','plain','utf-8')
# #发送HTML邮件
# # msg = MIMEText('<html><body><h1>Hello</h1>' +
# #     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
# #     '</body></html>', 'html', 'utf-8')
# #发送带附件的邮件
# msg = MIMEMultipart()
# msg['From'] = _formate_addr('Python爱好者 <%s>' % from_addr)
# msg['To'] = _formate_addr('管理员 <%s>' % to_addr)
# msg['Subject'] = Header('来自SMTP的问候。。。','utf-8').encode()
# #邮件正文
# # msg.attach(MIMEText('hello,send by python...','plain','utf-8'))
# #带有图片的邮件正文
# msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
#     '<p><img src="cid:0"></p>' +
#     '</body></html>', 'html', 'utf-8'))
# #添加附件就是加一个MIMEBase,从本地读一个文件
# with open('icon.jpg','rb') as f:
#     mime = MIMEBase('image','jpg',filename='icon.jpg')
#     mime.add_header('Content-Disposition','attachment',filename='icon.jpg')
#     mime.add_header('Content-ID','<0>')
#     mime.add_header('X-Attachment-Id','0')
#     mime.set_payload(f.read())
#     encoders.encode_base64(mime)
#     msg.attach(mime)
# server = smtplib.SMTP(smtp_server,25)
# server.set_debuglevel(1)
# server.login(from_addr,password)
# server.sendmail(from_addr,[to_addr],msg.as_string())
# server.quit()

import sqlite3

# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# # cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
# cursor.execute('insert into user (id,name) values (\'3\',\'Michael\')')
# # print(cursor.rowcount())
# cursor.execute('select * from user where id=?',('1',))
# values = cursor.fetchall()
# print(values)
# cursor.close()
# conn.commit()
# conn.close()
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001','Adam',95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()