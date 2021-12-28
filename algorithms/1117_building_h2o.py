#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2021/12/28 下午8:15
# desc:
import threading
from threading import Thread, RLock, Lock


def releaseHydrogen():
    print('H')


def releaseOxygen():
    print('O')

import threading
class H2O:
    def __init__(self):
        self.h_sema = threading.Semaphore(2)
        self.o_sema = threading.Semaphore(1)
        self.h_num = 1

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        # self.h_lock.acquire()
        self.h_sema.acquire()
        releaseHydrogen()
        self.h_num += 1
        if self.h_num == 2:
            self.h_num = 0
            self.o_sema.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.o_sema.acquire()
        releaseOxygen()
        self.h_sema.release()
        self.h_sema.release()


if __name__ == '__main__':
    obj = H2O()
    for _ in range(3):
        t1 = Thread(target=obj.hydrogen, args=(releaseHydrogen,))
        t2 = Thread(target=obj.oxygen, args=(releaseOxygen,))

        t2.start()
        t1.start()

        t1.join()
        t2.join()
