def a1():
    for i in range(5):
        if i == 2:break
        print(i)
    else:
        print("end")

def a2():
    for i in range(5):
        if i == 2:continue
        print(i)
    else:
        print("end")

def b1():
    try:
        a = 1/0
        print("error")
        return a
    except Exception as e:
        print(e)
    else:
        print("else")
    finally:
        a = 1
        print("finally")

def b2():
    try:
        a = 1
        print("okay")
        return a
    except Exception as e:
        print(e)
    else:
        print("else")
    finally:
        a = 2
        print("finally")


if __name__ == '__main__':
    a1()
    print()
    a2()
    print()
    print(b1())
    print()
    print(b2())
