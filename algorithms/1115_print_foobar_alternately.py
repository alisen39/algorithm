#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2021/12/26 下午5:10
# desc: 
from threading import Thread
from threading import Lock


class FooBar:
    def __init__(self, n):
        self.n = n
        self.lockFoo = Lock()
        self.lockBar = Lock()
        # self.lockBar.acquire()
        # self.lockBar.release()

        self.lockBar.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.lockFoo.acquire()
            printFoo()
            self.lockBar.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.lockBar.acquire()
            printBar()
            self.lockFoo.release()


def printBar():
    print('bar')


def printFoo():
    print('foo')


if __name__ == '__main__':
    fb = FooBar(3)

    t1 = Thread(target=fb.foo, args=(printFoo,))
    t2 = Thread(target=fb.bar, args=(printBar,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
