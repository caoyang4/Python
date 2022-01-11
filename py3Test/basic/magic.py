# encoding: utf-8
import time, datetime


def get_business_days(start_time):
    now_time = time.strftime("%Y-%m-%d %H:%M:%S")
    now_time = datetime.datetime.strptime(now_time, "%Y-%m-%d %H:%M:%S")
    start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    tag_date = start_time
    while True:
        if tag_date > now_time:
            break
        if tag_date.weekday() in [5, 6]:
            yield tag_date
        tag_date += datetime.timedelta(1)


# start = "2021-10-17 11:19:42"
# work_days = len(list(get_business_days(start)))
# print work_days


class X:
    def __init__(self, a):
        self.a = a
        self.a["a"] = 1


class A(object):
    def __init__(self, ):
        self.a = 1
        self.b = 2
        self.c = 3

    def __repr__(self):
        return "A[]"

    def __str__(self):
        return "A.__str__"

    def __call__(self, *args, **kwargs):
        print("__call__")

    def add(self):
        self.a += 1
        self.__xx()
        return self.a

    def __getattr__(self, item):
        print("__getattr__")
        return "NotFound"

    def __getattribute__(self, item):
        print("__getattribute__")
        return object.__getattribute__(self, item)

    def __xx(self):  # 不提供外部调用，不被子类继承使用
        print(self.a)

    def _y(self):    # 不提供外部调用，可以被子类继承使用
        print(self.b)


class B(A):
    def __init__(self):
        super(B, self).__init__()

    def y(self):
        self._y()


if __name__ == '__main__':
    a = A()
    a()
    # a()  # 调用__call__方法
    # print(a)
    # print(a.__dict__)
    # print(a.a)  # 调用属性，会调用该函数
    # print(a.z)  # 不存在的属性、方法调用__getattr__
    # a.add()

    bb = B()
    bb.y()



