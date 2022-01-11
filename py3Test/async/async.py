import asyncio
import time
import unittest


async def _test1():
    print("step1")
    await asyncio.sleep(1)
    print("step2")


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def _test2():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


async def _test3():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def _test4():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)


class MyTestCase(unittest.TestCase):

    def test1(self):
        asyncio.run(_test1())

    def test2(self):
        asyncio.run(_test2())

    def test3(self):
        asyncio.run(_test3())

    def test4(self):
        asyncio.run(_test4())
