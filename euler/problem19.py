"""
def isLeap(year):
	if year % 4==0:
		if year%100==0:
			return [31,28,31,30,31,30,31,31,30,31,30,31]
		elif year%400==0:
			return [31,29,31,30,31,30,31,31,30,31,30,31]
		else:
			return [31,29,31,30,31,30,31,31,30,31,30,31]
	else:
		return [31,28,31,30,31,30,31,31,30,31,30,31]

DAY=[x for range(1,7)]
"""
import calendar
print sum([1 for y in range(1901,2001) for m in range(1,13) if calendar.weekday(y, m, 1)==6])