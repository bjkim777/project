"""
#python3
from math import gcd
from functools import reduce
print(reduce(lambda x, y: int(x*y/gcd(x,y), range(1,21))))
"""

i=0
j=0

while j!=21:
	i+=20
	j=2
	while j<=20:
		if i%j==0:
			j+=1
		else:
			break

print(i)