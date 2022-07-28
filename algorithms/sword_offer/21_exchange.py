#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/7/28 22:53
# desc:
""" 剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/
"""
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        p1, p2 = 0, len(nums) - 1
        while p1 < p2:
            # p1 指向偶数，p2指向奇数，调换顺序
            while p1 < p2 and nums[p1] % 2 == 1:
                p1 += 1
            while p1 < p2 and nums[p2] % 2 == 0:
                p2 -= 1

            nums[p1], nums[p2] = nums[p2], nums[p1]

        return nums


if __name__ == '__main__':
    res = Solution().exchange([1, 2, 4, 3])
    print(res)
