#-*-coding:utf8 -*-
#  animal，runnable(mixin), flyable(mixin)


class Animal(object):
    def __init__(self):
        super(Animal, self).__init__()
        print "I am animal."


class RunnableMixin(object):
    def __init__(self):
        super(RunnableMixin, self).__init__()
        print "I can run."


class FlyableMixin(object):
    def __init__(self):
        super(FlyableMixin, self).__init__()
        print "I can fly."


class Dog(RunnableMixin, Animal):
    def __init__(self):
        print "I am a dog."
        super(Dog, self).__init__()

d = Dog()