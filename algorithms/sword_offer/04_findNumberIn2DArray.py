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
        if not matrix:
            return False
        x, y = 0, len(matrix[0])-1
        while True:
            if x > len(matrix)-1 or y < 0:
                return False

            if target == matrix[x][y]:
                return True
            elif target < matrix[x][y]:
                y -= 1
            elif target > matrix[x][y]:
                x += 1


if __name__ == '__main__':
    arr = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    arr = []
    r = Solution().findNumberIn2DArray(arr, target=31)
    print(r)
