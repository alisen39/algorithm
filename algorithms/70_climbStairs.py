#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2022年06月28日 星期二
# desc:
from functools import lru_cache


class Solution:
    @lru_cache()
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(0))
    print(s.climbStairs(1))
    print(s.climbStairs(2))
    print(s.climbStairs(3))
    print(s.climbStairs(4))
    print(s.climbStairs(44))
