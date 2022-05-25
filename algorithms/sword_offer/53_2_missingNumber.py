#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/5/25 23:09
# desc:
""" 剑指 Offer 53 - II. 0～n-1中缺失的数字
https://leetcode.cn/problems/que-shi-de-shu-zi-lcof/
"""
from typing import List

class Solution:
    # TODO 可用二分法
    def missingNumber(self, nums: List[int]) -> int:
        target = 0
        for i in nums:
            if i == target:
                target += 1
                continue
            else:
                return target
        else:
            return target


if __name__ == '__main__':
    # nums = [0, 1, 2, 3, 4]
    # nums = [0]
    nums = [1]
    nums = []
    n = Solution().missingNumber(nums)
    print(n)
