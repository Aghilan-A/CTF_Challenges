import dis
x = "QUNOQ1RGe1NuNGtlX2J5dDNfYzBkZX0="
flag = "ACNCTF{Sn4ke_byt3_c0de}"
def sssssswitch(l1,l2):
	a = ord(l1)
	b = ord(l2)
	a = a+b
	b = a-b
	a = a-b
	return (chr(a)+chr(b))

def anna_con_da(x):
	this_one_or_that_one = ""
	for i in range(0,len(x),2):
		if i != len(x)-1:
			this_one_or_that_one += sssssswitch(x[i],x[i+1])
	return this_one_or_that_one
ct = anna_con_da(x)
print(ct)
bytecode = dis.dis(anna_con_da)
#bytecode1 = dis.dis(this_to_that)