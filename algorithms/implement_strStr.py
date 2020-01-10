#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/1/10 9:45 
# @Author : Alisen 
# @File : implement_strStr.py
'''

    28. 实现 strStr()
    https://leetcode-cn.com/problems/implement-strstr/
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        for i in range(len(haystack) - len(needle) + 1):
            right = len(needle) + left

            if haystack[left:right] == needle:
                return i
            else:
                left += 1
        return -1


if __name__ == '__main__':
    # haystack = 'hello'
    # needle = 'lo'
    haystack = 'aaaaa'
    needle = 'bba'

    res = Solution().strStr(haystack, needle)
    print(res)
