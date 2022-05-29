#!/usr/bin/env python
# encoding: utf-8
# author: Alisen

""" 剑指 Offer 11. 旋转数组的最小数字
https://leetcode.cn/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
"""
import time
from json.tool import main
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left, right = 0, len(numbers) - 1
        while left < right:

            m = (left + right) // 2
            if numbers[m] > numbers[right]:
                left = m + 1
            elif numbers[m] < numbers[right]:
                right = m
            elif numbers[m] == numbers[right]:
                right -= 1
        return numbers[left]


if __name__ == "__main__":
    numbers = [3, 4, 5, 1, 2]
    # numbers = [2, 2, 0, 1]
    # numbers = []
    # numbers = [3, 1]
    # numbers = [1]
    numbers = [5, 1, 3]

    res = Solution().minArray(numbers)
    print(res)
