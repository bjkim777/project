sum=1
for a in range(1,100):
	sum*=a

sum2=0
for index in range(len(str(sum))):
	sum2+=int(str(sum)[index])
print(sum2)
	
