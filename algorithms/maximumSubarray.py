#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/1/14 15:22 
# @Author : Alisen 
# @File : maximumSubarray.py
'''
    53. 最大子序和
    https://leetcode-cn.com/problems/maximum-subarray/
'''


class Solution:
    def maxSubArray(self, nums: list) -> int:
        max_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            max_sum = max(nums[i], max_sum)
        return max_sum

if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = Solution().maxSubArray(nums)
    print(res)