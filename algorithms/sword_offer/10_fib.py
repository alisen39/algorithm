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
    @lru_cache()
    def fib(self, n: int) -> int:
        n = n % 1000000007
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)%1000000007


if __name__ == '__main__':
    res = Solution().fib(45)
    print(res)
