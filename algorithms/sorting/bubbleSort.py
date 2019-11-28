#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/11/28 15:56 
# @Author : Alisen 
# @File : bubble_sort.py

''' 二、
    冒泡排序
        时间复杂度 O(n^2) 空间复杂度 O(n)

    1. 遍历列表，比较当前值与下一个值的大小
        如果当前值大于下一个值，则交换位置，否则 下一步
        （这样做可以把最大的值放到最后一个，所以下次遍历只需遍历n-1个值即可）
    2. 重复第一步 n次

'''


class Solution:
    def bubble(self, disorder_arr: list):
        for i in range(len(disorder_arr)):
            for j in range(len(disorder_arr) - i-1):

                if disorder_arr[j] > disorder_arr[j+1]:
                    temp = disorder_arr[j]
                    disorder_arr[j] = disorder_arr[j+1]
                    disorder_arr[j+1] = temp
        return disorder_arr


if __name__ == '__main__':
    # arr = []
    # arr = [1]
    # arr = [2, 1]
    # arr = [1, 2]
    arr = [92, 1, 21, 10, 0, -10, -1, 101, 2, 2, 10]

    res = Solution().bubble(arr)
    print(res)
