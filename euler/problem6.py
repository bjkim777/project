data = range(1,101)
print ( sum(data)**2 - sum(map(lambda x: x**2, data)) )