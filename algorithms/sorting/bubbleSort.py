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
            for j in range(len(disorder_arr) - i - 1):

                if disorder_arr[j] > disorder_arr[j + 1]:
                    temp = disorder_arr[j]
                    disorder_arr[j] = disorder_arr[j + 1]
                    disorder_arr[j + 1] = temp

                # print(i, j, disorder_arr)

        return disorder_arr

    def bubble2(self, disorder_arr: list):
        team = len(disorder_arr) - 1

        i = 0
        while i < team:
            if disorder_arr[i] > disorder_arr[i + 1]:
                temp = disorder_arr[i]
                disorder_arr[i] = disorder_arr[i + 1]
                disorder_arr[i + 1] = temp
            # print(team, i, disorder_arr)

            if i == team - 1:
                i = -1
                team -= 1

            i += 1
        return disorder_arr


if __name__ == '__main__':
    import time
    import random
    # arr = []
    # arr = [1]
    # arr = [2, 1]
    # arr = [1, 2]
    # arr = [92, 1, 21, 10, 0, -10, -1, 101, 2, 2, 10]
    arr = [random.randint(-10000, 10000) for i in range(1000)]

    # res = Solution().bubble(arr)
    # res = Solution().bubble2(arr)

    s1_time = time.time()
    res = Solution().bubble(arr.copy())
    # print(res)
    print('s1 speed time:', time.time() - s1_time)

    s2_time = time.time()
    res = Solution().bubble2(arr.copy())
    # print(res)
    print('s2 speed time:', time.time() - s2_time)

    print(res)
