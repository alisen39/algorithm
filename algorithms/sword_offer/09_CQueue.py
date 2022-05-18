#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/5/18 22:41
# desc:
""" 剑指 Offer 09. 用两个栈实现队列
https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
"""


class CQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def appendTail(self, value: int) -> None:
        self.in_stack.append(value)

    def deleteHead(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            return -1
        return self.out_stack.pop()


if __name__ == '__main__':
    obj = CQueue()
    param_2 = obj.deleteHead()
    print(param_2)
    obj.appendTail('1')
    param_2 = obj.deleteHead()
    print(param_2)
    param_2 = obj.deleteHead()
    print(param_2)

    obj.appendTail('2')
    obj.appendTail('3')
    param_2 = obj.deleteHead()
    print(param_2)
    param_2 = obj.deleteHead()
    print(param_2)
