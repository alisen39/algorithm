#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/1/19 16:29 
# @Author : Alisen 
# @File : isDuplicate.py
'''

存在重复
https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/24/
'''


class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        return len(nums) != len(set(nums))

if __name__ == '__main__':
    # nums = [1, 2, 3]
    nums = [1,2,3,1]
    nums = []
    res = Solution().containsDuplicate(nums)
    print(res)
