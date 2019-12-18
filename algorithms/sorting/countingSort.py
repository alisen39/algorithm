#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2019-12-18 23:02

class Solution:
    '''
    计数排序
    只能针对整数排序

    将原数组的值，转换为新数组的下标

    '''

    def counting(self, arr):

        if arr is None or arr == []:
            return arr
        mx = max(arr) # 找到最大值与最小值
        mn = min(arr)
        bias = mn # 最小值为偏移量

        new_arr = [0] * (mx - mn+1) # 生成一个新的计数数组
        for item in arr:
            new_arr[item - bias] += 1

        # print(new_arr)

        result = []
        for i in range(len(new_arr)):
            for j in range(new_arr[i]):
                result.append(i+bias)
        print(result)
        return arr


if __name__ == '__main__':
    import random
    import time

    # arr = []
    # arr = [1]
    # arr = [2, 1]
    # arr = [1, 2]
    # arr = [92, 1, 21, 10, 0, -10, -1, 101, 2, 2, 10]

    arr = [random.randint(-10000, 10000) for i in range(100000)]
    res = Solution().counting(arr.copy())
