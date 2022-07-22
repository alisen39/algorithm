#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/7/22 22:42
# desc:
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def gen_tree_node(node_list: List[int]):
    node_queue = []  # 不满的节点
    root_node = TreeNode(node_list.pop(0))
    node_queue.append(root_node)
    while node_list:
        tmp_node = node_queue.pop(0)

        left_node = TreeNode(node_list.pop(0))
        right_node = TreeNode(node_list.pop(0))
        tmp_node.left = left_node
        tmp_node.right = right_node
        node_queue.append(tmp_node.left)
        node_queue.append(tmp_node.right)
    return root_node


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def gen_list_node(arr: List):
    l = ListNode(-1)
    head = l
    for item in arr:
        l.next = ListNode(item)
        l = l.next
    return head.next


def parse_list_node(list_node: ListNode):
    arr = []
    while list_node:
        arr.append(list_node.val)
        list_node = list_node.next
    return arr
