#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/11/29 16:54 
# @Author : Alisen 
# @File : binarySearch.py
'''
    704. 二分查找
'''


class Solution:
    def search(self, nums: list, target: int):
        left = 0
        right = len(nums) - 1
        if target > nums[right] or target < nums[left]:
            return -1

        while left < right:
            mid = int((right+left+1) /2)
            if target >= nums[mid]:
                left = mid
            else:
                right = mid-1
        if nums[left] != target:
            return -1
        return left


if __name__ == '__main__':
    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # arr = [-1,0,3,5,9,12]
    arr = [-1,0,3,5,9,12]
    res = Solution().search(arr, 0)
    print(res)
