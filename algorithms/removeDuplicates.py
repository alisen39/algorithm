#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2019-12-22 19:54

'''

    删除排序数组中的重复项

    https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

'''


class Solution:
    def removeDuplicates(self, nums: list):
        p = 1
        while p < len(nums):
            if nums[p] == nums[p - 1]:
                nums.pop(p)
            else:
                p += 1

        print(nums)
        return len(nums)


if __name__ == '__main__':
    # arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    arr = [0, 0, 0]

    Solution().removeDuplicates(arr)
