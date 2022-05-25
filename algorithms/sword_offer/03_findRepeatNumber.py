#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/5/25 22:33
# desc:
""" 剑指 Offer 03. 数组中重复的数字
https://leetcode.cn/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
"""
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        per = None
        for i in nums:
            if i == per:
                return i
            else:
                per = i


if __name__ == '__main__':
    nums = [1, 2, 21, 11, 1]
    res = Solution().findRepeatNumber(nums)
    print(res)
