#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/5/22 15:06
# desc:
""" 剑指 Offer 06. 从尾到头打印链表
https://leetcode.cn/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reversePrint(self, head: ListNode) -> List[int]:
        arr = []

        has_next = True
        while has_next:
            if not head:
                break
            arr.insert(0, head.val)
            if not head.next:
                break
            head = head.next

        return arr


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(6)
    l3 = ListNode(None)
    l4 = ListNode(5)
    l3.next = l4
    l2.next = l3
    l1.next = l2
    a = Solution().reversePrint(l1)
    print(a)
