#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/12/19 18:33 
# @Author : Alisen 
# @File : isPowerOfThree.py
'''
    3的幂
    https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/25/math/62/
'''


class Solution:
    # def isPowerOfThree(self, n: int) -> bool:
    #     # 使用递归解答
    #     if n < 1:
    #         return False
    #     elif n == int(1):
    #         return True
    #     else:
    #         return self.isPowerOfThree(n / 3)

    # def isPowerOfThree(self, n: int) -> bool:
    #     # 使用循环解答
    #     while n > 0:
    #         if n <1:
    #             return False
    #         elif n == int(1):
    #             return True
    #         else:
    #             n/=3

    def isPowerOfThree(self, n: int) -> bool:
        # 使用乘法解答
        base = 1
        while base != n:
            base *= 3
            if base == n:
                return True
            elif base >n:
                return False
        return True

if __name__ == '__main__':
    # n = 0
    n = 1
    # n = 3
    # n = -1
    # n = 10
    res = Solution().isPowerOfThree(n)
    print(res)
