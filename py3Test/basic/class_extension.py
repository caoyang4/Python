# encoding: utf-8


class A:
    def __init__(self, a):
        self.a = a*2


class B(A):
    def __init__(self, a):
        self.a = a

b = B(2)
print(b.a)