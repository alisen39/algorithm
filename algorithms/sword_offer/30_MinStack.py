#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/5/18 23:00
# desc:
""" 剑指 Offer 30. 包含min函数的栈
https://leetcode.cn/problems/bao-han-minhan-shu-de-zhan-lcof/
"""
from collections import deque


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.in_stack = deque([])
        self.min_stack = deque([])

    def push(self, x: int) -> None:
        self.in_stack.append(x)
        if not self.min_stack or self.min_stack[-1] >= x:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.in_stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        if self.in_stack:
            return self.in_stack[-1]
        return

    def min(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return


if __name__ == '__main__':
    obj = MinStack()
    obj.push(0)
    obj.push(1)
    obj.push(0)
    param_3 = obj.top()
    param_4 = obj.min()
    print(param_3, param_4)

    obj.pop()
    param_3 = obj.top()
    param_4 = obj.min()
    print(param_3, param_4)
