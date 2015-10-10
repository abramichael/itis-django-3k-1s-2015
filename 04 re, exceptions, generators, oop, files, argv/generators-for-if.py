
# generators
s = "aaaadeaaaaaafaaaddaaaaee"
print "".join([chr(ord(x) + 1) for x in s if x != 'a'])
