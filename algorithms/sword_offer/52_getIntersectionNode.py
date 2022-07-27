#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/7/22 22:36
# desc:

""" 面试题52. 两个链表的第一个公共节点
https://leetcode.cn/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/
"""
from algorithms.utils.list_node import gen_list_node, parse_list_node


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        htb = set()
        tmp = headA
        while tmp:
            htb.add(tmp)
            tmp = tmp.next

        tmp = headB
        while tmp:
            if tmp in htb:
                return tmp
            tmp = tmp.next



if __name__ == '__main__':
    l1 = gen_list_node([0, 9, 1, 2, 4])
    l2 = gen_list_node([3, 2, 4])
    res = Solution().getIntersectionNode(l1, l2)
    print(parse_list_node(res))
