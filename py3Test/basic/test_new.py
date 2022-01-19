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


a = A("abc")
b = A("xyz")
print(id(a))
print(id(b))


class demoClass:
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


test1 = demoClass("abc")
test2 = demoClass("xyz")
print(test1.number, test1.instances_created)
print(test2.number, test2.instances_created)
