from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long

p2 = getPrime(1024)
q2 = getPrime(1024)
N2 = p2 * q2
phi = (p2-1) * (q2-1)

while True:
	d = getPrime(256)
	e = pow(d,-1,phi)
	if e.bit_length()==N2.bit_length():
		break
flag = bytes_to_long(b'ct : 596226742521621113825006949939118096370521904690942144211928527028561242346506036995881515020610058575625')

ct2 = pow(flag,e,N2)
# print(ct2)

# ##### Decryption -2 
# import owiener
# d = owiener.attack(e,N2)
# print(long_to_bytes(pow(ct2,d,N2)))


e1 = 21

p1 = getPrime(4096)
q1 = getPrime(4096)

N1 = p1*q1

m = bytes_to_long(b"ACNCTF{w1en3r_4nd_c00p3r5m1th_4r3_fri3333nd555}")

ct1 = pow(m,e1,N1)

print(f'N1 : {N2}')
print(f'd : {d}')
print(f'ct1 : {ct2}')
print(f'N2 : {N1}')
print(f'e2 : {e1}')
print(f'ct2 : {ct1}')
# ###Decryption - 1
# from gmpy2 import iroot
# print(bytes.fromhex(hex(iroot(ct1, e1)[0])[2:]))
