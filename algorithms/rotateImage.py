#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/1/13 15:47 
# @Author : Alisen 
# @File : rotateImage.py
'''
    48. 旋转图像
    https://leetcode-cn.com/problems/rotate-image/
'''


class Solution:
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            # matrix[i].reverse()
            print(matrix)
        for i in range(len(matrix)):
            matrix[i].reverse()



if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    Solution().rotate(matrix)
