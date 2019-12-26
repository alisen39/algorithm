#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/12/2 18:16 
# @Author : Alisen 
# @File : searchInsertPlace.py

'''
    搜索插入位置
    https://leetcode-cn.com/problems/search-insert-position/solution/er-fen-cha-zhao-bian-jie-jie-shi-qing-song-zhang-w/
'''


class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right +1) >> 1
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid
        if nums[left] < target:
            return left+1
        return left


if __name__ == '__main__':
    arr = []
    arr = [1, 2, 3, 5]
    # arr = [5, 6, 7]
    # arr = [1, 3, 5, 6]
    # arr = [1,3,6]

    res =  Solution().searchInsert(arr,4)
    print(res)