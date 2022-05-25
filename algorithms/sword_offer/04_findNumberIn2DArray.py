#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/5/25 23:28
# desc:
""" 剑指 Offer 04. 二维数组中的查找
https://leetcode.cn/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
"""
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        for list1 in matrix:
            if not list1:
                continue
            if target < list1[0] or target > list1[-1]:
                continue
            for i in list1:
                if i == target:
                    return True
        return False



if __name__ == '__main__':
    arr = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    r = Solution().findNumberIn2DArray(arr, target=100)
    print(r)
