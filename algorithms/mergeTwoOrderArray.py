#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/12/3 16:02 
# @Author : Alisen 
# @File : mergeTwoOrderArray.py

'''
合并两个有序数组
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/8/sorting-and-searching/52/
'''


class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:

                nums1[p] = nums1[p1]
                p1 -= 1
            else:

                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]

        print(nums1)


if __name__ == '__main__':
    # nums1 = [1, 2, 3, 0, 0, 0]
    # nums2 = [2, 3, 5]
    nums1 = [4, 5, 6, 0, 0, 0]
    nums2 = [1, 2, 7]

    Solution().merge(nums1, 3, nums2, len(nums2))
