#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2019-11-27 21:25

''' 三
    快速排序
        冒泡排序的基础上进行的改进

'''


class Solution:
    def selection(self, disorder_arr: list):
        pass

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
