#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2021/12/22 下午10:50
# desc:
from threading import Thread
from threading import Lock


class Foo:
    def __init__(self):
        self.firstLock = Lock()
        self.secondLock = Lock()
        self.firstLock.acquire()
        self.secondLock.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstLock.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self.firstLock:
            printSecond()
            self.secondLock.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self.secondLock:
            printThird()


def printThird():
    print('third')


def printSecond():
    print('second')


def printFirst():
    print('first')


if __name__ == '__main__':
    foo = Foo()
    t1 = Thread(target=foo.first, args=(printFirst,))
    t2 = Thread(target=foo.second, args=(printSecond,))
    t3 = Thread(target=foo.third, args=(printThird,))
    t3.start()
    t1.start()
    t2.start()
