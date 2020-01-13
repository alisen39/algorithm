#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/1/13 14:44 
# @Author : Alisen 
# @File : countAndSay.py
'''
    38. 外观数列
    https://leetcode-cn.com/problems/count-and-say/
'''


class Solution:

    def countAndSay(self, n: int) -> str:
        if n <= 1:
            return '1'
        pre = self.countAndSay(n - 1)

        res = ''
        count = 1
        for idx in range(len(pre)):

            if idx == 0:
                count = 1

            elif pre[idx] != pre[idx - 1]:
                tmp = str(count) + pre[idx - 1]
                res += tmp
                count = 1
            elif pre[idx] == pre[idx - 1]:
                count += 1

            if idx == len(pre) - 1:
                tmp = str(count) + pre[idx]
                res += tmp
        return res


if __name__ == '__main__':
    n = 5
    res = Solution().countAndSay(n)
    print(res)
