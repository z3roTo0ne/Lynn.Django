class MyLocker(object):
    def __init__(self):
        print("{}.__init__() has been called.".format(self.__class__.__name__))

    @staticmethod
    def acquire():
        print("MyLocker.acquire() has been called.")

    @staticmethod
    def unlock():
        print("MyLocker.unlock() has been called.")


class LockRex(MyLocker):
    @staticmethod
    def acquire():
        print("LockRex.acquire() has been called")

    @staticmethod
    def unlock():
        print("LockRex.unlock() has been called.")


def lockhelper(cls):
    def _deco(func):
        def __deco(*args, **kwargs):
            print("before %s called." % func.__name__)
            cls.acquire()
            try:
                return func(*args, **kwargs)
            finally:
                cls.unlock()
        return __deco
    return _deco


class Example(object):
    @lockhelper(MyLocker)
    def myfunc(self):
        print("myfunc() has been called.")

    @lockhelper(MyLocker)
    @lockhelper(LockRex)
    def myfunc2(self, a, b):
        print("myfunc2() has been called.")
        return a + b

if __name__ == "__main__":
    e = Example()
    e.myfunc()
    print("#"*30)
    print(e.myfunc())
    print("#" * 30)
    print(e.myfunc2(3,4))
