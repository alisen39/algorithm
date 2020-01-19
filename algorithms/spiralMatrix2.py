#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/1/19 15:22 
# @Author : Alisen 
# @File : spiralMatrix2.py
class Solution:
    def generateMatrix(self, n: int):
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        # print(matrix)

        left = 0
        right = len(matrix[0]) - 1
        top = 0
        buttom = len(matrix) - 1
        i = 0
        j = 0

        k = 0

        while left <= right and top <= buttom:

            while j <= right:
                k += 1
                matrix[i][j] = k
                j += 1
            j -= 1

            i += 1
            while i <= buttom:
                k += 1
                matrix[i][j] = k
                i += 1
            i -= 1

            top += 1
            if left < right and top <= buttom:
                while j > left:
                    j -= 1
                    k += 1
                    matrix[i][j] = k

                while i > top:
                    i -= 1
                    k += 1
                    matrix[i][j] = k

                j += 1

            right -= 1
            buttom -= 1
            left += 1
        return matrix


if __name__ == '__main__':
    n = 3
    res = Solution().generateMatrix(n)
    print(res)
