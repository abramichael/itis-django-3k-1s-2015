auth = False

def check(f):
    global auth
    def wrapper():
        if auth:
            print "yeah, you cat see it!"
            f()
        else:
            print "oops"
    return wrapper

@check
def f():
    print "Secret"

f()