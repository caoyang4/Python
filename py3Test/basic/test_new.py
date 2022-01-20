# encoding: utf-8

class A:
    """
        单例
        http://c.biancheng.net/view/5484.html
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        print("__new__():", cls, args, kwargs)
        print("__instance: ", A.__instance)
        if A.__instance is None:
            A.__instance = super().__new__(cls)
        return A.__instance

    def __init__(self, attribute):
        print("__init__():", self, attribute)
        self.attribute = attribute


print("A test")
a1 = A("abc")
a2 = A("xyz")
a3 = A("abc")
print(id(a1))
print(id(a2))
print(id(a3))


class B:
    instances_created = 0

    def __new__(cls, *args, **kwargs):
        print("__new__():", cls, args, kwargs)
        instance = super().__new__(cls)
        instance.number = cls.instances_created
        cls.instances_created += 1
        return instance

    def __init__(self, attribute):
        print("__init__():", self, attribute)
        self.attribute = attribute


print("\n")
print("B test")
b1 = B("abc")
b2 = B("abc")
b3 = B("abc")
print(id(b1))
print(id(b2))
print(id(b3))
print(b1.number, b1.instances_created)
print(b2.number, b2.instances_created)
print(b3.number, b3.instances_created)


class C:
    __instance = None

    def __init__(self, attribute):
        if C.__instance is None:
            print("__init__")
        self.attribute = attribute


print("\n")
print("C test")
c1 = C("abc")
c2 = C("abc")
print(id(c1))
print(id(c2))

