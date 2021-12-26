#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2021/10/20 下午11:58
# desc: 将数组中奇数放到后面

class Solution:
    def change(self, arr: list):
        n = len(arr)-1
        idx = 0
        while idx <= n:
            if arr[idx] % 2 == 1:
                tmp = arr.pop(idx)
                arr.append(tmp)
                n -= 1
                continue
            idx += 1
        return arr


if __name__ == '__main__':
    # arr = []
    arr = [1, 2, 3, 4, 5]
    # arr = [1, 1, 1, 1, 1, 2, 3]
    res = Solution().change(arr)
    print(res)
