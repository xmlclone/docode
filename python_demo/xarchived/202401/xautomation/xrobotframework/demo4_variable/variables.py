import os

# email_host在rf里面就可以通过${email_host}进行引用，这里获取的是环境变量TG_EMAIL_ACCOUNT的值
email_host = os.getenv('TG_EMAIL_ACCOUNT')