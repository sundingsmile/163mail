import smtplib
from email.mime.text import MIMEText
from email.header import Header

class Mail(object):
    def __init__(self,msg_to_list=['sundingsmile@163.com'],mail_dic={'Name': ['sunding'], 'Subject': ['1'], 'Email': ['sdfadf@qq.com'], 'Phone': ['17736041156'], 'Message': ['test']}):
        self.msg_from = 'sundingsmile@163.com'  # 发送方邮箱
        self.passwd = 'gq2007431066'  # 填入发送方邮箱的授权码(填入自己的授权码，相当于邮箱密码)
        self.msg_to_list = msg_to_list
        self.content = "\r\n".join([x + ':'+mail_dic[x][0] for x in mail_dic.keys()])
        self.msg = MIMEText(self.content)
        self.msg['Subject'] = mail_dic.get('Subject')[0]  # 邮件主题
        self.msg['From'] = mail_dic.get('Name')[0] + '<sundingsmile@163.com>' # 放入发件人
        self.msg['To'] = 'Myself<sundingsmile@163.com>'  # 放入收件人

    def send_mail(self):
        try:
            mail_client = smtplib.SMTP_SSL('smtp.163.com',465)  # 通过ssl方式发送，服务器地址，端口
            mail_client.login(self.msg_from, self.passwd)  # 登录到邮箱
            mail_client.sendmail(self.msg_from, self.msg_to_list, self.msg.as_string())  # 发送邮件：发送方，收件方，要发送的消息
            print('成功')
        except Exception as e:
            print(e)
        finally:
            mail_client.quit()

if __name__ == '__main__':
    test = Mail()
    test.send_mail()