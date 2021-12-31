#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2021/12/31 上午8:31
# desc: 

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        n_sum = 1
        d = 2
        while d * d <= num:
            if num % d == 0:
                n_sum += d
                if d * d < num:
                    n_sum += num / d
            d += 1
        return n_sum == num


if __name__ == '__main__':
    num = 3

    r = Solution().checkPerfectNumber(num)
    print(r)
