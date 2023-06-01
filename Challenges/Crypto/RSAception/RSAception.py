#####---RSAception------##########
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
e1 = 1
p1 = getPrime(1024)
q1 = getPrime(1024)
N1 = p1 * q1

message1 = 'REDACTED'
message1 = bytes_to_long(message1)
ct1 = pow(message1,e1,N1)

flag = 'REDACTED'
e2 = 65537
N2 = 2140324650240744961264423072839333563008614715144755017797754920881418023447140136643345519095804679610992851872470914587687396261921557363047454770520805119056493106687691590019759405693457452230589325976697471681738069364894699871578494975937497937
ct2 = pow(flag,e2,N2)

print(f'e1 : {e1}')
print(f'N1 : {N1}')
print(f'ct1 : {ct1}')
print(f'e2 : {e2}')
print(f'N2 : {N2}')
