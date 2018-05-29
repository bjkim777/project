from math import sqrt

def eratosthenes(limit):
	lst=range(2,limit)
	for i in range(2, int(sqrt(limit))+1):
		lst = filter(lambda x: x==i or x %i, lst)
	return lst

print sum(eratosthenes(2000000))