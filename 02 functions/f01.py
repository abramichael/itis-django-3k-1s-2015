#!/usr/bin/python
# -*- coding: utf-8 -*-

# Тест

def f(x, y):
	"""
	This is my cool function that does addition	
	:param x: arg1
	:param y: arg2
	"""
	return x + y
	
print f(1, 2)
print f("abc", "def")
help(f)

g = 9.86
def gravity(m):
	global g
	return m * g

print gravity(10)