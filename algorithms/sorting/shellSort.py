#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2019-12-08 17:55

'''
    5. 希尔排序
    1959年Shell发明，第一个突破O(n2)的排序算法，是简单插入排序的改进版。它与插入排序的不同之处在于，它会优先比较距离较远的元素。希尔排序又叫缩小增量排序。

    h=3*b+1
    b = 1

'''


class Solution:

    def shell(self, disorder_arr: list):
        gap = 1
        while gap < len(disorder_arr) / 3:
            gap = 3 * gap + 1

        while gap >= 1:
            for i in range(gap, len(disorder_arr)):
                if disorder_arr[i] > disorder_arr[i - gap]:
                    continue

                j = i
                while j > 0 and disorder_arr[j] < disorder_arr[j - gap]:
                    disorder_arr[j], disorder_arr[j - gap] = disorder_arr[j - gap], disorder_arr[j]

                    j -= gap
                print(disorder_arr)
            print(gap)
            gap = int((gap - 1) / 3)
        return disorder_arr

    # def insertion(self, disorder_arr: list):
    #
    #     for i in range(1, len(disorder_arr)):
    #
    #         if disorder_arr[i] > disorder_arr[i - 1]:
    #             continue
    #
    #         for j in range(i):
    #             if disorder_arr[i] < disorder_arr[j]:
    #                 disorder_arr.insert(j, disorder_arr.pop(i))
    #
    #     return disorder_arr


if __name__ == '__main__':
    import random
    import time

    # arr = []
    # arr = [1]
    # arr = [2, 1]
    # arr = [1, 2]
    # arr = [92, 1, 21, 10, 0, -10, -1, 101, 2, 2, 10]

    arr = [random.randint(-10000, 10000) for i in range(100000)]
    res = Solution().shell(arr.copy())

    # s1_time = time.time()
    # res = Solution().shell(arr.copy())
    # # print(res)
    # print('s1 speed time:', time.time() - s1_time)

    print(res)
