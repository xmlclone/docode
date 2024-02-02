import base64

from cffi import FFI

ffi = FFI()

# 定义 CFFI 的接口
ffi.cdef("""
    void encrypt(char* data, char* key);
""")
ffi.cdef("""
    void decrypt(char* data, char* key);
""")

# 加载 C 代码并编译为模块
mylib = ffi.dlopen("libencry.so")

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