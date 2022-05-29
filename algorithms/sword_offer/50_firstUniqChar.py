#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/5/29 23:28
# desc:
""" 剑指 Offer 50. 第一个只出现一次的字符
https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/
"""
from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> str:
        hmap = defaultdict(int)
        for item in s:
            hmap[item] += 1
        for item in s:
            if hmap[item] == 1:
                return item
        return ' '


if __name__ == '__main__':
    # s = 'abbcdeffdec'
    s = ''
    res = Solution().firstUniqChar(s)
    print(res)
