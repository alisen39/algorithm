#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/5/24 20:00
# desc:
""" 剑指 Offer 58 - II. 左旋转字符串
https://leetcode.cn/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/
"""


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        for i in range(n):
            s += s[i]
        return s[n:]


if __name__ == '__main__':
    s = 'abcdefg'
    n = 2
    res = Solution().reverseLeftWords(s, n)
    print(res)
