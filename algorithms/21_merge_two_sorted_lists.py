#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2021/12/18 下午10:00
# desc:
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


if __name__ == '__main__':
    list1 = ListNode(1, ListNode(2, ListNode(5)))
    list2 = ListNode(0, ListNode(2, ListNode(4)))
    res = Solution().mergeTwoLists(list1, list2)
    # res = list2
    while 1:
        print(res.val)
        if res.next is None:
            break
        res = res.next
