#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/5/22 15:26
# desc:
""" 剑指 Offer 24. 反转链表
https://leetcode.cn/problems/fan-zhuan-lian-biao-lcof/
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return

        pre_node = None
        curr = head

        while curr:
            tmp = curr.next
            curr.next = pre_node
            pre_node = curr
            curr = tmp
        return pre_node


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(6)
    l3 = ListNode(None)
    l4 = ListNode(5)
    l3.next = l4
    l2.next = l3
    l1.next = l2
    a = Solution().reverseList(l1)

    while True:
        print(a.val)
        if not a.next:
            break
        a = a.next
