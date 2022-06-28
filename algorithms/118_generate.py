#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/6/28 16:14
# desc:
""" https://leetcode.cn/problems/pascals-triangle/
118. 杨辉三角
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        for i in range(1, numRows + 1):
            ret2 = []
            for j in range(1, i + 1):
                if j == 1 or j == i:
                    ret2.append(1)
                else:
                    ret2.append(ret[i - 2][j - 2] + ret[i - 2][j - 1])
            ret.append(ret2)
        return ret


if __name__ == '__main__':
    print(Solution().generate(5))
