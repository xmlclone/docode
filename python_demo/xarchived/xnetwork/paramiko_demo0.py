"""
利用paramiko传输文件
"""

import paramiko

# 创建SSH客户端
client = paramiko.SSHClient()

# 如果远程主机没有在本机的known_hosts文件中
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接到远程主机
client.connect(hostname='远程主机IP地址', username='用户名', password='密码')

# 创建SFTP会话
sftp = client.open_sftp()

# 上传文件
sftp.put('本地文件路径', '远程文件路径')

# 下载文件
sftp.get('远程文件路径', '本地文件路径')

# 关闭SFTP会话
sftp.close()

# 关闭SSH连接
client.close()