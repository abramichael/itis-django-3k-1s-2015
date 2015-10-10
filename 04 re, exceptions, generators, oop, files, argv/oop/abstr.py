import abc

class Animal:
    __metaclass__ = abc.ABCMeta

    def voice(self):
        print "Hawk!"


class Dog(Animal):
    pass


a = Dog()
a.voice()

