#coding: utf-8
import this
print
print "hello"
print 'hello'
print """
as;dflkajs;dflj
a;djfa;sldfkja;lsdf
asd;fkjas;d
"""
print(1)
print(1L)
a = 2
a = "abc"
a = 1.5
b = 13
print a + b
print a ** b
print int(a)
print str(b)
x = 5
if x > 0:
    pass
elif x == 0:
    pass
elif x != 0: #<> deprecated
    pass

i = 1
while (i < 10):
    print range(100)
    print xrange(200)
    i += 5

s = []
s.append(1)
t = range(1,100,3)
print t

s = (1, 2)
s = {"hello": 3, "bye":5}
for key, value in s.iteritems():
    print key, value
for key in s.keys():
    print key, s[key]

# import math
# from math import *

s = 1.5 + 0.5j

print s.imag

st = "abc"
print st * 10
st[1:3]
print st[1:3]


x = range(10)
dir(x)
for y in x[:]:
    if y % 2 == 0:
        x.insert(0, 'a')
print x