"""
NUM={1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
	11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eigthteen', 19:'nineteen',
	20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eigthty', 90:'ninety'}

LENTH=0
for num in range(1,1001):
	CONV=str(num)
	if len(CONV)==1:
		LENTH+=len(NUM[num])
		print (CONV)
	elif len(CONV)==2:
		if int(CONV[-2])==1:
			LENTH+=len(NUM[num])
			print (CONV)
		else:
			if int(CONV[-1])==0:
				LENTH+=len(NUM[num])
				print (CONV)
			else:
				LENTH+=len(NUM[int(CONV[-2])*10]+ NUM[int(CONV[-1])])
				print (CONV)
	elif len(CONV)==3:
		HUNDRED='hundred'
		if CONV[-2:]=='00':
			LENTH+=len(NUM[int(CONV[-3])]+HUNDRED)
			print (CONV)
		else:
			if int(CONV[-2])==1:
				LENTH+=len(NUM[int(CONV[-3])]+HUNDRED+'and'+NUM[int(CONV[-2:])])
				print (CONV)
			elif int(CONV[-2])==0:
				LENTH+=len(NUM[int(CONV[-3])]+HUNDRED+'and'+NUM[int(CONV[-1])])
				print (CONV)
			else:
				if int(CONV[-1])!=0:
					LENTH+=len(NUM[int(CONV[-3])]+HUNDRED+'and'+NUM[int(CONV[-2])*10]+NUM[int(CONV[-1])])
					print (CONV)
				else:
					LENTH+=len(NUM[int(CONV[-3])]+HUNDRED+'and'+NUM[int(CONV[-2])*10])
					print (CONV)
	else:
		LENTH+=len('onethousand')
		print (CONV)
print(LENTH)
"""	
def tostr(N):
    if N == 1000:
        return 'onethousand'
    elif N >= 100:
        if N % 100 == 0: return tostr(N/100)+'hundred'
        else:            return tostr(N/100)+'hundredand' + tostr(N%100)
    elif N >= 20:    
        return ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninty'][N/10-2]+tostr(N%10)
    else:
        return ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'][N]

print sum([len(tostr(n)) for n in range(1, 1001)])