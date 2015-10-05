

def f(*args):
	s = 0
	for item in args:
		s += item
	return s
		
print f(10,20,30)
print f(1,2,5,10,72,3)

lst = (1,2,5,2,8,2,3)
print f(*lst)


	

