#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/7/22 20:36
# desc:

""" 剑指 Offer 25. 合并两个排序的链表
https://leetcode.cn/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        pre = head
        while l1 and l2:
            if l1.val > l2.val:
                pre.next = l2
                l2 = l2.next

            else:
                pre.next = l1
                l1 = l1.next
            pre = pre.next
        if l1 is None:
            pre.next = l2
        if l2 is None:
            pre.next = l1
        pre = pre.next
        return head.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(7)
    l1.next = l2
    l2.next = l3

    l11 = ListNode(1)
    l22 = ListNode(3)
    l33 = ListNode(6)
    l11.next = l22
    l22.next = l33

    Solution().mergeTwoLists(l1, l11)
