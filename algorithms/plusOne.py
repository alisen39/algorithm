#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2020-01-15 22:47

'''
    66. 加一
    https://leetcode-cn.com/problems/plus-one/
'''


class Solution:
    int
    # def plusOne(self, digits: list):
    #     for i in range(len(digits)):
    #         idx = len(digits) - i - 1
    #         num_sum = digits[idx] + 1
    #         p = num_sum // 10
    #         if p > 0:
    #             digits[idx] = 0
    #
    #         else:
    #
    #             digits[idx] += 1
    #             break
    #     else:
    #         digits.insert(0,1)
    #     return digits
    def plusOne(self, digits: list):
        for i in range(len(digits)):
            idx = len(digits) - i -1
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                break
        if digits[0] == 0:
            digits.insert(0, 1)

        return digits

if __name__ == '__main__':
    digits = [1, 2, 3]
    # digits = [0]
    # digits = [9]
    # digits = [9, 9]
    # digits = [8, 9, 9, 9]

    res = Solution().plusOne(digits)
    print(res)
