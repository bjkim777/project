def count_factors(num):
	loop=num**0.5

	if loop==int(loop):
		count=1
	else:
		count=0

	i=1

	while i<loop:
		if num%i==0:
			count+=2
		i+=1
	return count

i=1; tri_num=0
while True:
	tri_num=tri_num+i
	count=count_factors(tri_num)

	if count >=500:
		print(tri_num)
		break
	i+=1
