#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/11/25 9:28 
# @Author : Alisen 
# @File : longestPalindromicSubstring.py
# @link : https://leetcode-cn.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        if s is None or len(s) <= 0:
            return ''

        for i in range(len(s)-1):  # 如果第 n-1 个与第 n 个不是回文，那么反之亦然。故长度为n-1
            # 中心为一个字母
            l1, r1 = self.expend(s, i, i)

            l2, r2 = self.expend(s, i, i + 1)
            # l1, r1 = l2,r2
            if r1 - l1 > r2 - l2 :
                r, l = r1, l1
            else:
                r, l = r2, l2

            if r - l > end - start:
                start = l
                end = r
        if start == end:
            end += 1
        return s[start:end]

    def expend(self, x, left, right):

        # if x[left] != x[right]:
        #     return left, right + 1

        while left >= 0 and right < len(x) and x[left] == x[right]:
            left -= 1
            right += 1
        return left+1,right-1+1

        #
        # while left > 0 and right < len(x):
        #     if x[left] == x[right] and x[left - 1] == x[right + 1]:
        #         left -= 1
        #         right += 1
        #     else:
        #         break
        # return left, right + 1


if __name__ == '__main__':
    # test_case = {
    #     'babad': ['bab', 'aba'],
    #     'xabax': 'xabax',
    #     'xabbx': 'bb',
    #     'xabbax': 'xabbax',
    #     'xabay': 'aba',
    #     'cbbd': 'bb',
    #     'ccc': 'ccc',
    #     'cccc': 'cccc',
    #     'c': 'c',
    #     'cd': ['c','d'],
    # }
    # for k, v in test_case.items():
    #     print(k, v)
    #     res = Solution().longestPalindrome(k)
    #     if res not in v and res != v:
    #         print(k, v,res)
    #         assert False

    s = 'c'
    res = Solution().longestPalindrome(s)
    print(res)
