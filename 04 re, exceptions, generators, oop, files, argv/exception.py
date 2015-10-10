def fact(n):
    if not isinstance(n, int):
        raise TypeError("Wanna INT!")
    if n < 0:
        raise ValueError("Can't resolve n! when n is negative")
    return reduce(lambda x, y: x * y, xrange(1, n+1))

x = "fact"
try:
    print fact(x)
except ValueError, e:
    print "Catched!", e
    print (e)
except TypeError, e:
    print "TUPY DANNYHHHH!"
else:
    print "Don't worry, be happy"
finally:
    print "Finally"

