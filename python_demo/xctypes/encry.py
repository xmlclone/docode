import ctypes
import base64


# 加载动态库
mylib = ctypes.cdll.LoadLibrary("./libencry.so")

# 定义参数和返回值类型
mylib.encrypt.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
mylib.encrypt.restype = None

mylib.decrypt.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
mylib.decrypt.restype = None

# 定义固定密钥
secure_key = "99abc".encode()


def encrypt(src: str | bytes, secure_key):
    encrypted_bytes = src.encode()
    mylib.encrypt(encrypted_bytes, secure_key)
    encrypted_bytes = base64.b64encode(encrypted_bytes)
    encrypted_string = encrypted_bytes.decode('utf-8')
    return encrypted_string

def decrypt(src: str | bytes, secure_key):
    encrypted_bytes = src.encode('utf-8')
    decrypted_bytes = base64.b64decode(encrypted_bytes)
    mylib.decrypt(decrypted_bytes, secure_key)
    return decrypted_bytes.decode()

enc = encrypt("hello, worldx!", secure_key)
print(f"{enc=}")
dec = decrypt(enc, secure_key)
print(f"{dec=}")