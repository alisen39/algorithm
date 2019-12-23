#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2019-12-23 23:16
'''
    移除元素
    https://leetcode-cn.com/problems/remove-element/submissions/
'''
class Solution:
    def removeElement(self, nums: list, val: int) -> int:

        p = 0
        while p < len(nums):
            if nums[p] == val:
                nums.pop(p)
            else:
                p+=1
        return p

if __name__ == '__main__':
    arr = [0,1,2,2,3,0,4,2]
    arr = [3,2,2,3]
    # arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # arr = [0, 0, 0]

    res = Solution().removeElement(arr,3)
    print(res)

