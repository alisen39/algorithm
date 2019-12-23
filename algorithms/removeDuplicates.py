#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2019-12-22 19:54

'''

    删除排序数组中的重复项

    https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

'''


class Solution:
    # def removeDuplicates(self, nums: list):
    #     p = 1
    #     while p < len(nums):
    #         if nums[p] == nums[p - 1]:
    #             nums.pop(p)
    #         else:
    #             p += 1
    #
    #     print(nums)
    #     return len(nums)

    def removeDuplicates(self, nums: list):
        p = 0
        for i in range(1, len(nums) ):
            if nums[i] != nums[p]:
                p += 1
                nums[p] = nums[i]

        # nums = nums[0:p+1]
        # print(nums)
        return p+1


if __name__ == '__main__':
    # arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    arr = [0, 0, 0]

    res = Solution().removeDuplicates(arr)
    print(res)
