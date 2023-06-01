from Crypto.Util.number import *
from Crypto.Cipher import AES
import random
import hashlib

flag = 'REDACTED'


with open("6b616f6e6173686931344d.txt",encoding="utf8") as f:
	words = [w.strip() for w in f.readlines()]

i = random.choice(words)
print(i)
key = hashlib.md5(i.encode()).digest()
print(len(key))
print(f'key : {key.hex()}')
cipher = AES.new(key,AES.MODE_ECB)
ciphertext = cipher.encrypt(flag)
print(ciphertext.hex())

