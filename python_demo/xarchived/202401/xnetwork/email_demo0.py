import smtplib
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_html_mail(
    host: str, 
    sender: str, 
    sender_passwd: str, 
    to_list: list[str],
    subject: str,
    content: str,
    cc_list: list[str] = None,
    port: int=25
):
    """群发邮件功能

    :param host: 发件人SMTP服务器地址.
    :type host: str
    :param sender: 发件人账号.
    :type sender: str
    :param sender_passwd: 发件人密码.
    :type sender_passwd: str
    :param to_list: 收件人列表.
    :type to_list: list[str]
    :param subject: 邮件主题.
    :type subject: str
    :param content: 邮件内容, html格式.
    :type content: str
    :param cc_list: 抄送人列表.
    :type cc_list: list[str]
    :param port: 邮箱服务器Port.
    :type port: int
    """

    message = MIMEMultipart('related')
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = ';'.join(to_list)
    if cc_list:
        message["Cc"] = ';'.join(cc_list)
    message.attach(MIMEText(content, 'html', 'utf-8'))
    with smtplib.SMTP(host, port) as smtp:
        smtp.login(sender, sender_passwd)
        smtp.send_message(message)


passwd = os.environ.get("MYPASS")
send_html_mail(
    "mail.test.cn",
    "linlei@test.cn",
    passwd,
    ["linlei@test.cn"],
    "Test",
    "<h1>Test content</h1>"
)
