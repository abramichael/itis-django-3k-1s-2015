def f(x):
	return x*x
	
sqr = f

def super_f(f, x):
	return f(x)
	
print super_f(abs, -5)
print super_f(f, 5)

u = lambda x,y: x + y
#def u(x,y):
#	return x + y

print super_f(lambda x: x % 2, 5)

print (lambda x,y: x + y)(2,3)