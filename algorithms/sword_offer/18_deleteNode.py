#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/6/13 21:35
# desc:
""" 剑指 Offer 18. 删除链表的节点
https://leetcode.cn/problems/shan-chu-lian-biao-de-jie-dian-lcof/
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        pre = head
        while head:
            if head.val == val:
                pre = head.next
            if head.next and head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return pre


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3
    res = Solution().deleteNode(l1, 1)
    print(res.val)
