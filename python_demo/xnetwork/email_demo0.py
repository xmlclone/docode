from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

def send_mail(mail_host, mail_sender, mail_passwd, to_emailli, content):
    '''
        群发邮件功能
    :param mail_host: 发件人SMTP服务器地址
    :param mail_sender: 发件人账号
    :param mail_passwd: 发件人密码
    :param to_emailli: 收件人列表
    :param content: 邮件内容
    :return:
    '''
    msg = MIMEMultipart('related')
    msg["Subject"] = "Amber卡顿监控告警（{}--{}）" .format(start_time, end_time) # 邮件主题
    msg["From"] = mail_sender  # 发送人
    msg["To"] = ';'.join(to_emailli)  # 接收人

    msg.attach(MIMEText(content, 'html', 'utf-8'))

    ## 发送邮件
    try:
        s = smtplib.SMTP()  # 实例化对象
        s.connect(mail_host, 25)  # 连接邮箱服务器，端口号为25
        s.login(mail_sender, mail_passwd)  # 登录邮箱
        s.sendmail(mail_sender, to_emailli, msg.as_string())
        s.quit()
    except Exception as e:
        print(e)