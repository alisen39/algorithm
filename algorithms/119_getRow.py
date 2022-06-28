#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/6/28 16:14
# desc:
""" https://leetcode.cn/problems/pascals-triangle-ii/
119. 杨辉三角 II
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[List[int]]:
        ret = []
        for i in range(1, rowIndex + 2):
            ret2 = []
            for j in range(1, i + 1):
                if j == 1 or j == i:
                    ret2.append(1)
                else:
                    ret2.append(ret[i - 2][j - 2] + ret[i - 2][j - 1])
            ret.append(ret2)
        return ret[rowIndex]


if __name__ == '__main__':
    print(Solution().getRow(5))
