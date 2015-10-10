def fib():
    a = 0
    b = 1
    yield 1
    while True:
        c = a + b
        yield c
        b, a = c, b

i = 0
fib_gen = fib()
while (i < 10):
    print fib_gen.next()
    i += 1

