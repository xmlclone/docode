import binascii
import logging

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


logger = logging.getLogger(__name__)
key = 'abc15480ddloasd1'.encode('utf-8')
iv = '2f2f31d3528970632f2f31d352897063'.encode('utf-8')[:16]


def encrypt(word: str):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    data = word.encode('utf-8')
    padded_data = pad(data, AES.block_size)
    encrypted = cipher.encrypt(padded_data)
    return binascii.hexlify(encrypted).decode('utf-8')


def decrypt(word):
    encrypted_bytes = binascii.unhexlify(word)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted_bytes), AES.block_size)
    return decrypted.decode('utf-8')