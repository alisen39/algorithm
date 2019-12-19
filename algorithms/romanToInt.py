#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/12/19 18:29 
# @Author : Alisen 
# @File : romanToInt.py
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }

        result = 0
        for index,item in enumerate(s[::-1]):
            if item not in dic:
                assert None
            if index <=0:
                result += dic[item]
                continue
            if (item is 'I') and (s[::-1][index-1] is 'V' or s[::-1][index-1] is 'X'):
                result -= dic[item]
            elif (item is 'X') and (s[::-1][index-1] is 'L' or s[::-1][index-1] is 'C'):
                result -= dic[item]
            elif (item is 'C') and (s[::-1][index -1] is 'D' or s[::-1][index-1] is 'M'):
                result -= dic[item]
            else:
                result += dic[item]
        return result

if __name__ == '__main__':
    res = Solution().romanToInt("IVVIX")
    print(res)