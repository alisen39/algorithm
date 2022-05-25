#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/5/25 22:51
# desc:
""" 剑指 Offer 53 - I. 在排序数组中查找数字 I
https://leetcode.cn/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        cnt = 0
        for num in nums:
            if num == target:
                cnt += 1
        return cnt


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 5]
    res = Solution().search(a, 5)
    print(res)
