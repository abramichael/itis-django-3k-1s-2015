def print_date(year=1990, month=1, day=1):
	#print str(month) + "/" + str(day) + "/" + str(year)
	print "%s/%s/%s" % (month, day, year)
	
	
print_date(31) # 1/1/31 year
print_date(day=31) # 1/31/1990

def f(**kwargs):
	print kwargs.keys()
	
f(first_name="Andrew", last_name="Titov", patronym="Oleg uly")
	
d = {"a":5, "b":10}
f(**d)
d["abc"] = 100
f(**d)

def super_function(*args, **kwargs):
	pass

super_functions(1,"abc", abs, f=None, g=1)