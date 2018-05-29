num=[]

for x in range(100,1000):
	for y in range(100, 1000):
		z=x*y
		b=str(z)
		a=''.join(reversed(b))
		if b==a:
			num.append(b)

num2=[]

for item in num:
	raw = int(item)
	num2.append(raw)

num2.sort()
print(num2[-1])
		
