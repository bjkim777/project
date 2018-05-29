ipac=1
jpac=1
for i in range(1,41):
	ipac=i*ipac
for j in range(1,21):
	jpac=j*jpac
print (int(ipac/(jpac**2)))