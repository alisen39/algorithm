#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2019-11-20 23:12
'''
将矩阵中含有零的行和列设为0
'''


def yyqx(input_arr):
    cp_arr = input_arr.copy()
    height = len(input_arr)
    width = len(input_arr[0])

    for index, row in enumerate(input_arr):
        if 0 in row:
            cp_arr[index] = [0 for i in range(width)]

    for index in range(width):
        if 0 in [i[index] for i in input_arr]:
            for arr in cp_arr:
                arr[index] = 0
    return cp_arr


def yyqx_np(input_arr):
    import numpy as np
    input_arr = np.array(input_arr)
    cp_arr = input_arr.copy()
    col = np.prod(input_arr, axis=0)
    row = np.prod(input_arr, axis=1)
    for index, ha in enumerate(col):
        if ha == 0:
            cp_arr[:, index] = 0
    for index, li in enumerate(row):
        if li == 0:
            cp_arr[index] = 0
    return cp_arr


if __name__ == '__main__':
    input_arr = [[0, 2, 3, 9],
                 [3, 4, 5, 6],
                 [2, 0, 4, 5],
                 [4, 7, 9, 7]]

    # out = yyqx(input_arr)
    out_1 = yyqx_np(input_arr)
    # print(out)
    print(out_1)
