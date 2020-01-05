#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2020-01-05 21:07

'''

    https://leetcode-cn.com/problems/string-to-integer-atoi/
    字符串转换整数 (atoi)

'''
import re
class Solution:
    def myAtoi(self, s: str) -> int:

        p = '^ *(-?\+?\d+)'
        res = re.match(p,s)
        if res != None:
            return min(max(int(res.group(1).replace('+','')),-2**31),2**31-1)
        else:
            return 0
        # print(res)


if __name__ == '__main__':
    s = '123'
    s = '-123'
    s = '  -123'
    s = '-91283472332'
    s = '-+1'
    # s = '  0000000000012345678'


    res = Solution().myAtoi(s)
    print(res)
