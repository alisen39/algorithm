#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/1/14 18:01 
# @Author : Alisen 
# @File : lengthOfLastWord.py
'''
    58. 最后一个单词的长度
    https://leetcode-cn.com/problems/length-of-last-word/submissions/
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) <=0:return 0

        l = 0
        for i in s[::-1].lstrip(' '):
            if i != ' ':
                l +=1
            else:
                break
        return l
if __name__ == '__main__':
    # s = ''
    # s = ' '
    s = 's '
    # s = 's s'
    # s = 's ss'
    res =  Solution().lengthOfLastWord(s)
    print(res)