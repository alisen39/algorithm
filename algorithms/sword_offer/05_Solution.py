#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/5/24 19:51
# desc:
""" 剑指 Offer 05. 替换空格
https://leetcode.cn/problems/ti-huan-kong-ge-lcof/
"""


class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')


if __name__ == '__main__':
    a = 'x a xxx'
    a = '    '
    res = Solution().replaceSpace(a)
    print(res)
