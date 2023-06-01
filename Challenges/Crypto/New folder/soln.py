cipher_text = "55CGPAIQGP5DP6545C33D5NFXMZDYYV5NXFCMXZN&&PVPDXFFPTKDTKVZRYTHFLF"


hash_val = "99aff123de7cd765573304ece8c9eef2bc035b0a227c640765be2ad05e80f3e3"
key = "xor_i5_c00l"
flag = "ACNCTF{X0r_4s_4_5tr3am_Ciph3r}"
print(len(flag))
key_padded = ""

def pad(x,y):
	padded = ""
	while (len(padded) <= len(y)):
		for i in x:
			padded += i
	return padded
key_padded = pad(key,flag)
print(len(key_padded))


xored_output = "".join(chr(ord(i) ^ ord(j)) for i,j in zip(flag,key_padded))
print(xored_output)

f = open("D:\Aghilan\Amrita\CyberTechFest\Challenges\Crypto\RoXanne\out.txt", 'w')
f.write(xored_output)


