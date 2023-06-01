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
m1 = 'REDACTED'
ct1 = pow(m1,e,N2)
e1 = 21
p1 = getPrime(4096)
q1 = getPrime(4096)
N1 = p1*q1
flag = 'REDACTED'
ct2 = pow(flag,e1,N1)
print(ct1)
