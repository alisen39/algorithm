#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/12/12 15:59 
# @Author : Alisen 
# @File : heapSort.py
'''
堆排序
    堆是二叉树，
        每个结点的值都大于或等于其子结点的堆，称为大顶堆；
        每个结点的值都小于或等于其子结点的值，称为小顶堆。

    二叉树中，按层次遍历，若父节点的索引值为i,则左右子结点的索引值为 2*i+1 ,2*i+2
'''


class Solution:

    def heap(self, arr: list):
        for i in reversed(range(len(arr) >> 1)):
            self.heapAdjust(arr, i,len(arr))
            # print(i,arr)
        print(arr)

        for i in reversed(range(len(arr))):
            arr[0], arr[i] = arr[i], arr[0]
            print(i, arr)
            self.heapAdjust(arr, 0, i)
            print(i, arr)
        return arr

    def heapAdjust(self, arr, s: int, m: int):
        '''
        调整节点大小
        '''
        temp = arr[s]
        j = 2 * s + 1  # 左孩子节点
        # m = len(arr)
        while j < m:
            if j < m - 1 and arr[j] < arr[j + 1]:
                # j<m 判断左节点是否是唯一孩子
                # arr[j] < arr[j+1] 判断左孩子与右孩子的大小，取最大的一个
                j += 1

            if temp >= arr[j]:  # 如果temp > 最大的子孩子则结束循环
                break

            arr[s] = arr[j]

            if 2 * j + 1 <= m:
                s = j
                j = 2 * j + 1

            else:
                s = j
                break
        arr[s] = temp

        return arr


#   def heapChilds(self,arr,idx):
#     '''
#     输入一个数组，输入一个索引，输出孩子节点
#     '''
#     lChild = None
#     rChild = None
#     if (idx * 2 < len(arr)):
#
#         lChild = arr[idx * 2 + 1]
#         rChild = arr[idx * 2 + 2]
#     elif (idx * 2 == len(arr)):
#         lChild = arr[idx * 2 + 1]
#
#     return lChild, rChild


if __name__ == '__main__':
    import random
    import time

    # arr = []
    # arr = [1]
    # arr = [2, 1]
    # arr = [1, 2]
    arr = [92, 1, 21, 10, 0, -10, -1, 101, 2, 2, 10]

    # arr = [random.randint(-10000, 10000) for i in range(100000)]
    # res = Solution().heap(arr.copy())

    # s1_time = time.time()
    # res = Solution().shell(arr.copy())
    # # print(res)
    # print('s1 speed time:', time.time() - s1_time)

    # print(res)

    # res = Solution().heapChilds(arr.copy(), 2)

    # arr = [10, 20, 30, 40, 50]
    # print(arr)
    # res = Solution().heapAdjust(arr, 0)
    # print(res)

    arr = [10, 20, 30, 40, 50, 60, 70]
    print(arr)
    res = Solution().heap(arr)
    print(res)
