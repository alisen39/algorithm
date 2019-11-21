#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2019-11-21 22:53

'''
https://leetcode-cn.com/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode/
最长公共前缀
'''


class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''

        one = strs[0]

        for i in range(1, len(strs)):

            while strs[i] not in one or one.index(strs[i]) !=0:
                strs[i] = strs[i][0:-1]
            one = strs[i]

        return one


if __name__ == '__main__':
    res = Solution().longestCommonPrefix(['abcdefg', 'abc','ef'])
    print(res)
