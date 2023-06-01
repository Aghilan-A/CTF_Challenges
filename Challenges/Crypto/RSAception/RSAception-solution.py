#####---RSAception------##########
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
e1 = 1
p1 = getPrime(1024)
q1 = getPrime(1024)
N1 = p1 * q1


ciphertext1 = b"ct2 = 593954376080394201082212561433626454297891501658874054042768086660923352310965020458215995653036962080378740594174000762650702665917362256921050269504343200100355535112663938049983339900294077267488029723481615272770865141528035063121736655257563926"
message1 = bytes_to_long(ciphertext1)
ct1 = pow(message1,e1,N1)

##decrypt stage 1:
output1 = long_to_bytes(ct1)
print(f'output1 = {output1}')

flag = bytes_to_long(b"ACNCTF{CUr53D_B4bY_ToT1EnT_T0Y}")
p2 = 64135289477071580278790190170577389084825014742943447208116859632024532344630238623598752668347708737661925585694639798853367
q2 = 33372027594978156556226010605355114227940760344767554666784520987023841729210037080257448673296881877565718986258036932062711
e2 = 65537
N2 = p2 * q2
ct2 = pow(flag,e2,N2)


print(f'e1 : {e1}')
print(f'N1 : {N1}')
print(f'ct1 : {ct1}')
print(f'e2 : {e2}')
print(f'N2 : {N2}')