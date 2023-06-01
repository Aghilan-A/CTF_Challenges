cipher_text = "IB6M2CGCI&1QQF2G24MMG5PG6633CZGXYMC6MNXOPZXVYOGNTFYXYSEFPGZGSHLV"


hash_val = "3c0d50e010321e3c2400a4ba44114b9dd6325abf79acad59b6099ce53252afe8"
key = "xor_i5_c00l"
flag = "ACNCTF{X0r_4s_4_5tr3am_Ciph3r}"

key_padded = ""

def pad(x,y):
	padded = ""
	while (len(padded) <= len(y)):
		for i in x:
			padded += i
	return padded
key_padded = pad(key,flag)


xored_output = "".join(chr(ord(i) ^ ord(j)) for i,j in zip(flag,key_padded))
print(xored_output)

f = open("out.txt",'w')
f.write(xored_output)
# flag = "".join(chr(ord(i) ^ ord(j)) for i, j in zip(xored_output, key_padded))
# print(flag)

