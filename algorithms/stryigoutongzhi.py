#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2020-01-08 21:03
import sys

'''
    平安科技2020校招技术岗部分编程题
    https://www.nowcoder.com/profile/512111189/test/30143359/827778
    1. 判断字符串异构同质
'''

class Solution():
    def st(self, st):
        a1, a2 = st.split(' ')
        if len(a1) != len(a2):
            return False
        d1 = {}
        d2 = {}
        for i1,i2 in zip(a1,a2):
            print(i1,i2)
            if i1 not in d1:
                d1[i1] = 1
            else:
                d1[i1] += 1

            if i2 not in d2:
                d2[i2] = 1
            else:
                d2[i2] += 1
        if d1 != d2:
            print('false')
            return False
        else:
            print('true')
            return True



if __name__ == '__main__':
    # s = 'abc cba'
    # # s = 'aa cc'
    #
    # res = Solution().st(s)
    # print(res)

    # args = sys.argv[:]
    #
    # print(args[1])

    # res = Solution().st(args[1])
    # print(res)
    s = input()
    res = Solution().st(s)
    # print(res)