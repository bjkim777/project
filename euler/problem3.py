n,d = 600851475143,2
while d<n:
	while n%d is 0:
		n=n/d

	if n==1: break
	d=d+1
print (d)