x = 2
y = 3

def f(z):
	global x
	u = 10
	print locals()
	print globals()
	return x + u + z
	
print f(2)