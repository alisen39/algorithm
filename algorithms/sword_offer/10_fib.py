#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/7/7 22:54
# desc:
""" 剑指 Offer 10- I. 斐波那契数列
https://leetcode.cn/problems/fei-bo-na-qi-shu-lie-lcof/
"""

from functools import lru_cache


class Solution:
    # @lru_cache()
    # def fib(self, n: int) -> int:
    #     n = n % 1000000007
    #     if n == 0:
    #         return 0
    #     elif n == 1:
    #         return 1
    #     else:
    #         return self.fib(n - 1) + self.fib(n - 2)%1000000007

    def fib(self, n: int) -> int:
        a, b, c = 0, 1, 0
        if n < 2:
            return n
        while n >= 2:
            c = a + b
            a, b = b, c
            n -= 1
        return c % 1000000007


if __name__ == '__main__':
    # 0 0
    # 1 1
    # 2 1
    # 3 2

    # res = Solution().fib(46) # 836311896
    for _ in range(6):
        res = Solution().fib(_)  # 5
        print(_, res)
