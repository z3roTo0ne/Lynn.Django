#coding:utf8
"""
python的自省和反射
对于装饰器的反射，可以参考ftools.py
"""

import json
import inspect


# 下面这两行代码就是一个自省
methodList = [attr for attr in dir(json) if callable(getattr(json, attr))]
print(methodList)


def foo():
    who = inspect.getframeinfo(inspect.currentframe().f_back)[2]
    print("{} call me".format(who))


def a():
    foo()

def b():
    foo()

a()
b()
