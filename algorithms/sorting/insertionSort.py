#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2019-12-08 15:54

'''
    四、直接插入排序
    在有序数组里找到插入点
'''


class Solution:
    def insertion(self, disorder_arr: list):

        for i in range(1, len(disorder_arr)):  # 从第二个元素开始

            if disorder_arr[i] > disorder_arr[i - 1]:  # 判断当前元素与前一个元素的大小
                continue

            for j in range(i):  # 遍历当前元素之前的元素（有序），找到插入点插入
                if disorder_arr[i] < disorder_arr[j]:
                    disorder_arr.insert(j, disorder_arr.pop(i))
        return disorder_arr


if __name__ == '__main__':
    import random
    import time

    # arr = []
    # arr = [1]
    # arr = [2, 1]
    # arr = [1, 2]
    arr = [92, 1, 21, 10, 0, -10, -1, 101, 2, 2, 10]

    # arr = [random.randint(-10000, 10000) for i in range(10000)]

    s1_time = time.time()
    res = Solution().insertion(arr.copy())
    print(res)
    print('s1 speed time:', time.time() - s1_time)

    print(sorted(arr.copy()) == res)
