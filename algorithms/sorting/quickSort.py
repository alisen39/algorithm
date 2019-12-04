#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2019-11-27 21:25

''' 三
    快速排序
        基于分而治之的思想 时间复杂度为O(n logn)

'''


class Solution:

    def quick(self, disorder_arr: list):
        # 递归实现
        if len(disorder_arr) < 2:
            return disorder_arr

        base_num = disorder_arr[0]
        min_arr = []
        max_arr = []
        for i in range(1, len(disorder_arr)):
            if disorder_arr[i] <= base_num:
                min_arr.append(disorder_arr[i])
            elif disorder_arr[i] > base_num:
                max_arr.append(disorder_arr[i])

        return self.quick(min_arr) + [base_num] + self.quick(max_arr)


if __name__ == '__main__':
    import random
    import time

    # arr = []
    # arr = [1]
    # arr = [2, 1]
    # arr = [1, 2]
    # arr = [92, 1, 21, 10, 0, -10, -1, 101, 2, 2, 10]

    arr = [random.randint(-10000, 10000) for i in range(100000)]
    res = Solution().quick(arr)

    s1_time = time.time()
    res = Solution().quick(arr.copy())
    # print(res)
    print('s1 speed time:', time.time() - s1_time)

    # print(res)
