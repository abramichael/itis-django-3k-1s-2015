import random


class Phone:
    n = 0
    def __init__(self, model='HTC'):
        self.model = model
        self.__serial = random.randrange(1000)
        Phone.n += 1

    @staticmethod
    def working_with_n():
        print Phone.n

    @classmethod
    def working_with_class(cls):
        print dir(cls)


    def __str__(self):
        return "%s/%s" % (self.model, self.__serial)

    def call(self):
        print "Somebody is calling! (no but seriously)"

    def work(self):
        self.call()

class Camera:

    def __init__(self, model='Canon'):
        self.model = model
        self.__serial = random.randrange(1000)

    def make_photo(self):
        print "I am making the photo"

    def work(self):
        self.make_photo()

class SmartPhone(Phone, Camera):

    def __init__(self, model="Nexus"):
        Phone.__init__(self, model)
        self.google_name = random.randrange(10000)
        self.mode = True # calling mode, otherwise - False (photo)

    def work(self):
        if self.mode:
            Phone.work(self)
        else:
            Camera.work(self)

if __name__ == "__main__":
    p1 = Phone()
    p2 = Phone("Nokia")
    print p1.model
    print p2.model
    #print p1
    #print p2
    #p2.weight = 100
    #print p2.weight
    #print p1._Phone__serial
    print p1.n
    print p2.n
    Phone.n = 5
    print p2.n
