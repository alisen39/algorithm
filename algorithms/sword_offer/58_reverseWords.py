#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/7/28 23:22
# desc:
""" 剑指 Offer 58 - I. 翻转单词顺序
https://leetcode.cn/problems/fan-zhuan-dan-ci-shun-xu-lcof/
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        # lp, rp = 0, 0
        # s = s.strip()
        # res = []
        # for _ in range(len(s)):
        #     if s[_] == ' ' or _ == len(s)-1:
        #         res.insert(0, s[lp:rp])
        #         rp += 1
        #         lp = rp
        #     else:
        #         rp += 1
        # return ' '.join(res)

        # lp, rp = 0, 0
        # res = []
        # for _ in range(len(s)):
        #     rp += 1
        #     if s[rp] == ' ':
        #         res.insert(0, s[lp:rp])
        #         lp = rp
        #
        # return res
        stack = ''
        res = []
        for _ in s:
            if _ != ' ':
                stack += _
            elif _ == ' ' and not stack:
                continue
            else:
                res.insert(0, stack)
                stack = ''
        else:
            if stack:
                res.insert(0, stack)
        return ' '.join(res)


if __name__ == '__main__':
    res = Solution().reverseWords('asd.   dds asa. 1')
    print(res)
