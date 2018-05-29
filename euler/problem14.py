MAX=[0,0]

def collatz(num):
	count=1
	while True:
		if num%2==0:
			num=num/2
		elif num==1:
			return count
		else:
			num=3*num+1
		count+=1

for num in range(1,1000001):
	if MAX[0]<collatz(num):
		MAX=[collatz(num),num]
print(MAX)
