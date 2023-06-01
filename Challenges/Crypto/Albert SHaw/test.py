f = open("D:\Aghilan\Amrita\CyberTechFest\Challenges\Crypto\RoXanne\out.txt", 'r')
ct = f.read()
print(ct)
key_padded = 'xor_i5_c00lxor_i5_c00lxor_i5_c00l'
print(len(key_padded))
flag = "".join(chr(ord(i) ^ ord(j)) for i, j in zip(ct, key_padded))
print(flag)