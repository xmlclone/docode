import hashlib
import base64

# 定义一个密码（字符串）
password = 'my_password'

# 加密消息
def encrypt(message):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    md5_password = md5.digest()

    message_bytes = message.encode('utf-8')
    xor_bytes = bytearray()
    for i in range(len(message_bytes)):
        xor_bytes.append(message_bytes[i] ^ md5_password[i % len(md5_password)])

    encoded_bytes = base64.b64encode(xor_bytes)
    return encoded_bytes.decode('utf-8')

# 解密消息
def decrypt(encrypted):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    md5_password = md5.digest()

    encrypted_bytes = base64.b64decode(encrypted.encode('utf-8'))
    xor_bytes = bytearray()
    for i in range(len(encrypted_bytes)):
        xor_bytes.append(encrypted_bytes[i] ^ md5_password[i % len(md5_password)])

    return xor_bytes.decode('utf-8')

# 明文消息
message = 'Hello, world!'

# 加密
encrypted = encrypt(message)
print('Encrypted:', encrypted)

# 解密
decrypted = decrypt(encrypted)
print('Decrypted:', decrypted)