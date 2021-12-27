#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2021/12/27 下午9:18
# desc: 
from threading import Thread
from threading import Lock


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_lock = Lock()
        self.even_lock = Lock()
        self.odd_lock = Lock()

        self.even_lock.acquire()
        self.odd_lock.acquire()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(1, self.n + 1):

            if _ % 2 == 0:
                self.zero_lock.acquire()
                printNumber(0)
                self.even_lock.release()
            else:
                self.zero_lock.acquire()
                printNumber(0)
                self.odd_lock.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(1, self.n + 1):

            if _ % 2 == 0:
                self.even_lock.acquire()
                printNumber(_)
                self.zero_lock.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(1, self.n + 1):

            if _ % 2 != 0:
                self.odd_lock.acquire()
                printNumber(_)
                self.zero_lock.release()


def printNumber(x):
    if isinstance(x, int):
        print(x)


if __name__ == '__main__':
    obj = ZeroEvenOdd(5)

    t1 = Thread(target=obj.zero, args=(printNumber,))
    t2 = Thread(target=obj.even, args=(printNumber,))
    t3 = Thread(target=obj.odd, args=(printNumber,))

    t2.start()
    t3.start()
    t1.start()

    t1.join()
    t2.join()
    t3.join()
