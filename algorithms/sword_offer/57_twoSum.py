#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/7/28 23:16
# desc:
""" 剑指 Offer 57. 和为s的两个数字
https://leetcode.cn/problems/he-wei-sde-liang-ge-shu-zi-lcof/
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        i, j = 0, len(nums) - 1
        while i != j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] == target:
                return [nums[i], nums[j]]


if __name__ == '__main__':
    res = Solution().twoSum([1, 2, 3, 7], 10)
    print(res)
