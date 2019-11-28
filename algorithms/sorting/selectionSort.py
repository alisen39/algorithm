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


class Solution:
    def selection(self, disorder_arr: list):
        if len(disorder_arr) <= 0:
            return []

        result_arr = []
        for _ in range(len(disorder_arr)):

            min_num = disorder_arr[0]
            num_index = 0

            for index, item in enumerate(disorder_arr):
                if item < min_num:
                    min_num = item
                    num_index = index

            disorder_arr.pop(num_index)
            result_arr.append(min_num)

        return result_arr


if __name__ == '__main__':
    # arr = []
    # arr = [1]
    # arr = [2, 1]
    # arr = [1, 2]
    # arr = [92, 1, 21, 10, 0, -10, -1, 101, 2, 2, 10]
    import random
    arr = [random.randint(-10000,10000) for i in range(1000)]
    res = Solution().selection(arr)
    print(res)
