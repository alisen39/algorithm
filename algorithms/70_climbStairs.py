#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2022年06月28日 星期二
# desc:

class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1, 2, 3]
        if n < 3:
            return arr[n - 1]
        for i in range(n - 3):
            arr.append(arr[1] + arr[2])
            arr.pop(0)
        return arr[2]


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(0))
    print(s.climbStairs(1))
    print(s.climbStairs(2))
    print(s.climbStairs(3))
    print(s.climbStairs(4))
    print(s.climbStairs(10))
