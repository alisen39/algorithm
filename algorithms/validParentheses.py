#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2020-01-05 22:45

'''

有效的括号
https://leetcode-cn.com/problems/valid-parentheses/
'''


class Solution:
    def isValid(self, s: str) -> bool:
        # d = {'(': ')', '[': ']', '{': '}'}
        d = {')':'(',']':'[','}':'{'}
        st = []
        for i in range(len(s)):

            if s[i] in '([{':
                st.append(s[i])

            elif len(st)>0 and d[s[i]] == st[len(st) - 1]:
                st.pop(len(st) - 1)
            else:
                return False
        if len(st) == 0:
            return True
        else:
            return False

        # l_st = []
        # r_st = []
        # for i in range(len(s)):
        #     if s[i] in '([{':
        #         l_st.append(s[i])
        #     else:
        #         temp = d.get(s[i],None)
        #         if temp is None:
        #             return False
        #         r_st.append(temp)
        # if len(l_st) != len(r_st):
        #     return False
        #
        # for i in range(len(l_st)):
        #     if l_st[i] != r_st[i]:
        #         return False
        # return True
if __name__ == '__main__':
    s = ''
    # s = '('
    # s = '(]'
    # s = '((())]'
    # s = '()'
    # s = '()[]{}'
    # s = ']'
    # s = "([)]"

    res = Solution().isValid(s)
    print(res)
