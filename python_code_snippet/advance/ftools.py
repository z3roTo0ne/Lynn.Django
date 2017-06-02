#!/usr/bin/env python
# encoding: utf-8
from functools import update_wrapper
from functools import partial
from functools import wraps

# partial
def add(a ,b):
    return a+b

print("普通函数调用结果:{}".format(add(3,4)))
p1 = partial(add, 5)
print ("偏函数partial()的运算结果:{}".format(p1(6)))


# 普通的装饰器
def deco(func):
    def call_it(*args, **kwargs):
        """定义普通装饰器"""
        print('before call normal decorate.')
        return func(*args, **kwargs)
    return call_it

@deco
def hello():
    """调用普通装饰器"""
    print('normal decorate.')


# 带上update_wrapper()的装饰器
# 这个函数主要用在装饰器函数中，装饰器返回函数反射得到的是包装函数的函数定义而不是原始函数定义

def deco_with_update_wrapper(func):
    def call_it(*args, **kwargs):
        """定义functools.update_wrapper() 的装饰器"""
        print('before call update_wrapper().')
        return func(*args, **kwargs)
    return update_wrapper(call_it, func)

@deco_with_update_wrapper
def hello_update_wrapper():
    """调用functools.update_wrapper() 的装饰器"""
    print('decorate with update_wrapper().')


# 带上warp()的装饰器
def deco_with_wrap(func):
    @wraps(func)
    def _deco(*args, **kwargs):
        """定义functools.wrap() 的装饰器"""
        print("before call wrap().")
        return func(*args, **kwargs)
    return _deco


@deco_with_wrap
def hello_wrap():
    """调用 functools.wrap() 的装饰器"""
    print("decorate with wrap().")



if __name__ == '__main__':
    hello()
    print("hello.__name__ is: {}".format(hello.__name__))
    print("hello.__doc__ is:{}".format(hello.__doc__))

    hello_update_wrapper()
    print("hello_update_wrapper.__name__ is: {}".format(hello_update_wrapper.__name__))
    print("hello_update_wrapper.__doc__ is: {}".format(hello_update_wrapper.__doc__))

    hello_wrap()
    print("hello_wrap.__name__ is: {}".format(hello_wrap.__name__))
    print("hello_wrap.__doc__ is: {}".format(hello_wrap.__doc__))
