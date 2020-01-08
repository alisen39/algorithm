#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/1/8 9:12 
# @Author : Alisen 
# @File : containerWithMostWater.py
'''
    11. 盛水最多的容器
    https://leetcode-cn.com/problems/container-with-most-water/
'''


class Solution:
    def maxArea(self, height: list):
        start = 0
        end = len(height) - 1
        maxArea = 0
        while start < end:
            maxArea = max(maxArea, min(height[start], height[end]) * (end - start))
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1

        return maxArea


if __name__ == '__main__':
    arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    res = Solution().maxArea(arr)
    print(res)
