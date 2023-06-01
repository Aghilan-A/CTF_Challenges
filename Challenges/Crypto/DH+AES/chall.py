from Crypto.Util.number import *
from Crypto.Cipher import AES
import random
import hashlib

flag = b"ACNCTF{Br00t_4s}"


with open("D:\Aghilan\Amrita\CyberTechFest\Challenges\Crypto\DH+AES\kaonashi14M.txt", encoding="utf8") as f:
	words = [w.strip() for w in f.readlines()]

i = random.choice(words)
print(i)
key = hashlib.md5(i.encode()).digest()
print(len(key))
print(f'key : {key.hex()}')
cipher = AES.new(key,AES.MODE_ECB)
ciphertext = cipher.encrypt(flag)
print(ciphertext.hex())

# for i in words:
#     key = hashlib.md5(i.encode()).digest()
#     # print(key)
#     cipher = AES.new(key, AES.MODE_ECB)
#     decrypted = cipher.decrypt(ciphertext)
#     #print(decrypted)
#     if b"ACNCTF" in decrypted:
#         print(decrypted,i)
# g = 2
# p = getPrime(16)
# for i in range(2,p-2):
# 	if hex(pow(g,i,p)) == "11e421d53318b4c3ad81eb2f6787e398":
# 		print(i)
# # while True:
#     a = getRandomRange(2, p-2)
#     if GCD(a, p-1) == 1:
#     	break
# A = pow(g, a, p)
