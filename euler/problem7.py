prime=[2]
num=3

while len(prime) < 10001:
	n=1
	for p in prime:
		if num%p ==0:
			break
		else:
			if len(prime)==n:
				prime.append(num)
			else:
				n+=1
	num+=1
	
print(prime[-1])

