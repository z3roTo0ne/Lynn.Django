#!-*-coding:utf8-*-
import datetime
import time

# def deco(arg):
#     def _deco(your_function):
#         """ 使用内嵌包装函数来确保每次新函数都被调用，
#             内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象
#         """
#         def __deco(*args, **kwargs):
#             print u"函数 %s 被调用" % your_function.__name__
#             ret = your_function(*args, **kwargs)
#             return u"%s计算结果是%s" %  (arg, ret)
#         return __deco
#     return _deco
#
# @deco("haha")
# def myfunc(a, b):
#     return a + b
#
# @deco("hehe")
# def myfunc2(a, b ,c):
#     return  a + b + c
#
# print myfunc(3,4)
# print myfunc2(4,5,5)

from functools import wraps

func_cost_time = 0
def calculate_time(func):
    @wraps(func)
    def deco():
        global func_cost_time
        start = datetime.datetime.now()
        res = func()
        end = datetime.datetime.now()
        func_cost_time = end - start
        return res
    return deco

@calculate_time
def func():
    global func_cost_time
    time.sleep(1)
    print 'func1', func_cost_time

@calculate_time
def func2():
    global func_cost_time
    print 'func2', func_cost_time



if __name__ == '__main__':
    func()
    func2()