#print filter(function, list)

print filter(lambda x: x > 0, range(-10, 10, 2))

print map(lambda x: x * x, range(20))
print map(lambda x: x.upper(), ["ab", "itis", "kfu"])

print map(lambda x,y: x * y, range(10), range(0,20,2))

print reduce(lambda x, y: x - y, range(20))