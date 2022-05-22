#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/5/22 16:21
# desc:
""" 剑指 Offer 35. 复杂链表的复制
https://leetcode.cn/problems/fu-za-lian-biao-de-fu-zhi-lcof/
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return

        dic = {}
        curr = head
        while curr:
            dic[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            dic[curr].next = dic.get(curr.next)
            dic[curr].random = dic.get(curr.random)
            curr = curr.next
        return dic[head]


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(5)
    n3 = Node(3)
    n3.next = n2
    n3.random = None
    n2.next = n1
    n2.random = n3
    n1.next = None
    n1.random = n3
    a = Solution().copyRandomList(n3)
    while a:
        print(a.val, a.random)
        a = a.next
