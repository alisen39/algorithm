#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/7/22 20:19
# desc:

""" 剑指 Offer 22. 链表中倒数第k个节点
https://leetcode.cn/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p1, p2 = head, head
        p = 0
        while p2:
            if p >= k:
                p1 = p1.next
            p2 = p2.next
            p += 1
        return p1


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3
    res = Solution().getKthFromEnd(l1, 6)
    print(res.val)
