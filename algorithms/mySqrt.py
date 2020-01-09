#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2020-01-09 22:57

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x // 2 + 1  # 一个数的平方根最多不会超过它的一半

        while left < right:
            # +1为取右中位数，否则可能陷入死循环
            mid = (left + right + 1) >> 1
            square = mid * mid
            if square > x:
                right = mid - 1
            else:
                left = mid
        return left


if __name__ == '__main__':
    x = 10

    res = Solution().mySqrt(x)
    print(res)
