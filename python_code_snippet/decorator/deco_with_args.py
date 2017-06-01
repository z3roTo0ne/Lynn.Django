#!-*-coding:utf8-*-

def deco(arg):
    """
    简单总结就是：最外层是装饰器参数， 第2层参数就是你的函数， 最内层就是真正实现附加功能的地方
    :param arg:
    :return:
    """
    def _deco(your_function):
        """ 使用内嵌包装函数来确保每次新函数都被调用，
            内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象
        """
        def __deco(*args, **kwargs):
            print u"函数 %s 被调用" % your_function.__name__
            ret = your_function(*args, **kwargs)
            return u"%s计算结果是%s" %  (arg, ret)
        return __deco
    return _deco

@deco("haha")
def myfunc(a, b):
    return a + b

@deco("hehe")
def myfunc2(a, b ,c):
    return  a + b + c

print myfunc(3,4)
print myfunc2(4,5,5)