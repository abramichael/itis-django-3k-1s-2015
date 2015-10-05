import random


class Phone:

    def __init__(self, model='HTC'):
        self.model = model
        self.__serial = random.randrange(1000)

    def __str__(self):
        return "Cool phone from " + self.model

    def call(self):
        print "Somebody is calling! (no but seriously)"

p1 = Phone()
p2 = Phone("Nokia")
print p1.model
print p2.model
print p1
print p2

p2.weigth = 100
print p2.weigth

#print p1._Phone__serial
