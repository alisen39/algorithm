#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/1/19 10:58 
# @Author : Alisen 
# @File : spiralMatrix.py
'''
    54. 螺旋矩阵

    https://leetcode-cn.com/problems/spiral-matrix/solution/
'''


class Solution:
    def spiralOrder(self, matrix) -> list:
        if len(matrix)<=0:
            return []
        if len(matrix[0])<=0:
            return []
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        buttom = len(matrix) - 1
        i = 0
        j = 0

        res = []
        while left <= right and top <= buttom:

            while j <= right:
                res.append(matrix[i][j])
                print(matrix[i][j])
                j += 1
            j -= 1

            i += 1
            while i <= buttom:
                res.append(matrix[i][j])
                print(matrix[i][j])
                i += 1
            i -= 1

            top += 1
            if left < right and top <= buttom:
                while j > left:
                    j -= 1
                    res.append(matrix[i][j])
                    print(matrix[i][j])

            # if top < buttom:
                while i > top:
                    i -= 1
                    res.append(matrix[i][j])
                    print(matrix[i][j])

                j += 1


            right -= 1
            buttom -= 1
            left += 1
            print()
        return res


if __name__ == '__main__':
    matrix = [[10, 20, 30,100],
              [40, 50, 60,110],
              [70, 80, 90,120]]
    # matrix = [[10, 20, 30],
    #           [40, 50, 60],
    #           [70, 80, 90]]
    # matrix = [[10, 20, 30],
    #           [40, 50, 60],
    #           [70, 80, 90],
    #           [100, 110, 120]]

    # matrix = [[10, 20, 30, 130],
    #           [40, 50, 60, 140],
    #           [70, 80, 90, 150],
    #           [100, 110, 120, 160]]
    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    matrix = []
    res = Solution().spiralOrder(matrix)
    print(res)
