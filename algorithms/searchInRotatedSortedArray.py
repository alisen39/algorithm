#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2020-01-16 21:09

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/1/10 9:14
# @Author : Alisen
# @File : searchInRotatedSortedArray.py
'''
    33. 搜索旋转排序数组
    https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/
    思路：
        1. 首先使用二分查找，找到旋转数的下标
        2. 在选中的数组区域再次使用二分查找
'''


class Solution:
    def search(self, nums, target):
        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0
            while left <= right:
                pivot = (left + right) // 2  # 取左中位数
                if nums[pivot] > nums[pivot + 1]:

                    # 左中位数大于它右边的数的时候，返回右中位数的索引
                    # 例如：arr=[70,10] pivot=0 arr[pivot]>arr[pivot+1]=70>10
                    # 返回 10的下标，即1

                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        # 由于是中位数小于左边的判断，剔除了中位数本身等于目标值，因此右边界收敛时要减1，即减去自己。
                        # 例如：arr=[70,10,20] pivot=1 left=0 right=2 此时arr[1]<arr[pivot]=10<70
                        # 因此right =pivot-1 =1-1 =0 即可
                        right = pivot - 1
                    else:
                        #
                        left = pivot + 1
            # return pivot + 1

        def search(left, right):
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    # 判断中位数是否是目标值，
                    # 如果不是则返回-1
                    return pivot
                else:
                    if target < nums[pivot]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
            return -1

        n = len(nums)
        if n == 0: return -1  # 处理边界条件
        if n == 1: return 0 if nums[0] == target else -1

        rotate_index = find_rotate_index(0, n - 1)

        if nums[rotate_index] == target:
            return rotate_index

        if rotate_index == 0:
            # 如果数组是正常的，则按正常的二分查找做
            return search(0, n - 1)

        if target < nums[0]:
            # 在左边进行查找
            return search(rotate_index, n - 1)
        else:
            return search(0, rotate_index)


if __name__ == '__main__':
    # nums = [4, 5, 6, 7, 8, 9, 1, 2, 3]
    # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # nums = [4, 5, 6, 7, 0, 1, 2]
    # nums = [4]
    nums = [1, 3]

    target = 0
    res = Solution().search(nums, target)
    print(res)
