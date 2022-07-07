#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/7/7 22:54
# desc:
""" 剑指 Offer 10- II. 青蛙跳台阶问题
https://leetcode.cn/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
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

    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(1, n):
            a, b = b, a + b
        return b % 1000000007


if __name__ == '__main__':
    # 0 0
    # 1 1
    # 2 1
    # 3 2

    # res = Solution().fib(46) # 836311896
    for _ in range(9):
        res = Solution().numWays(_)  # 5
        print(_, res)
