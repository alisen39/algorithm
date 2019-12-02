#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2019-11-27 21:29

''' 一、
    选择排序
        最原始最传统的排序方法 时间复杂度 O(n^2) 空间复杂度 O(n)

    1. 遍历列表，找出最小的一个数
        保存第一个数，与后面的数依次对比，遇到比自己小的便记录下索引与数值
    2. 将最小的数添加到新的列表中，同时删除原数组中的数
    3. 重复第一步
'''
import time


class Solution:
    def selection(self, disorder_arr: list):
        # 稳定
        # 创建一个新列表，将最小值添加进新列表里
        result_arr = []
        for i in range(len(disorder_arr)):

            min_index = 0

            for index, item in enumerate(disorder_arr):
                if item < disorder_arr[min_index]:
                    min_index = index
            result_arr.append(disorder_arr[min_index])
            disorder_arr.pop(min_index)

        return result_arr

    def selection2(self, disorder_arr: list):
        # 稳定
        # 将最小值插入到原列表前面
        count = 0
        for j in range(len(disorder_arr) - 1):
            min_index = j

            for i in range(j, len(disorder_arr)):

                if disorder_arr[i] < disorder_arr[min_index]:
                    min_index = i
                count += 1

            disorder_arr.insert(j, disorder_arr[min_index])
            disorder_arr.pop(min_index + 1)
        print(count)
        return disorder_arr

    def selection3(self, disorder_arr: list):
        # 不稳定
        # 将最小值与当前值互换
        for j in range(len(disorder_arr) - 1):
            min_index = j

            for i in range(j, len(disorder_arr)):

                if disorder_arr[i] < disorder_arr[min_index]:
                    min_index = i
                # count += 1

            temp = disorder_arr[j]
            disorder_arr[j] = disorder_arr[min_index]
            disorder_arr[min_index] = temp

        return disorder_arr


if __name__ == '__main__':
    import random
    import time

    # arr = []
    # arr = [1]
    # arr = [2, 1]
    # arr = [1, 2]
    arr = [5, 8, 5, 2, 9]
    # arr = [92, 1, 21, 10, 0, -10, -1, 101, 2, 2, 10]
    # arr = [random.randint(-10000, 10000) for i in range(5000)]

    s1_time = time.time()
    res = Solution().selection(arr.copy())
    # print(res)
    print('s1 speed time:', time.time() - s1_time)

    s2_time = time.time()
    res = Solution().selection2(arr.copy())
    # print(res)
    print('s2 speed time:', time.time() - s2_time)

    s3_time = time.time()
    res = Solution().selection3(arr.copy())
    # print(res)
    print('s3 speed time:', time.time() - s3_time)

    # print(res)
