#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/7/12 21:00
# desc:
""" https://leetcode.cn/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
剑指 Offer 42. 连续子数组的最大和
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = []
        for i in range(len(nums)):
            if arr and arr[i - 1] >= 0:
                arr.append(arr[i - 1] + nums[i])
            elif not arr or arr[i - 1] <= 0:
                arr.append(nums[i])
        return max(arr)


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = Solution().maxSubArray(nums)
    print(res)
