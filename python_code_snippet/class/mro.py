import inspect

class A(object):
    def show(self):
        print("A.show()")

class B(A):
    pass

class C(A):
    def show(self):
        print("C.show()")

class D(B, C):
    pass

print(D.__mro__)
print(inspect.getmro(D))

d = D()
d.show()



