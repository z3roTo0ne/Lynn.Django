# coding=utf-8
# 《编写高质量代码的建议》 笔记
from __future__ import print_function


# python的字符串输出对比
def string_format():
    print("my name is %(name)s, my address is %(address)s" % {'name': 'chenlin', 'address': 'sichuan'})
    print("my name is {}, my address is {}".format('chenlin', 'sichuan'))


# 三元表达式
def sanyuan():
    x, y = 1, 2
    a = x if x < y else y
    print(a)


# case when
def fun_a():
    return "I am function a."


def fun_b():
    return "I am function b."


def f(x):
    return {
        0: fun_a(),
        1: fun_b()
    }.get(x, "you have not any agrs.")


# 断言
# 断言应该使用在正常逻辑不可到达的地方，和正常情况下总是为真的场合
def my_assert():
    x = 2
    assert x == 1, "not equals."


# 枚举替代
def enum(*args, **kwargs):
    return type("Enum", (object,), dict(zip(args, range(len(args))), **kwargs))


# 不推荐使用type来检查类型, 推荐types模块来判断
# python是弱类型的语言，在语言内部，根据需要进行了大量的隐式转换
def add(x,y):
    return x+y
print(add(1,2j))
print(add(1,2))
print(add('a','b'))
print(add(1.0,2.0))
print(add(1,'a'))  # 这里就会抛出异常， 不通过type来检查类型， 通过捕获异常来判断比较好


if __name__ == '__main__':
    pass


