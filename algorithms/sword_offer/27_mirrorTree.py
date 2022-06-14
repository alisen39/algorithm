#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/6/13 21:35
# desc:
""" 剑指 Offer 27. 二叉树的镜像
https://leetcode.cn/problems/er-cha-shu-de-jing-xiang-lcof/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        return root


if __name__ == '__main__':
    ta = TreeNode(3)
    ta_4 = TreeNode(4)
    ta_5 = TreeNode(5)
    ta_1 = TreeNode(1)
    ta_2 = TreeNode(2)
    ta.left = ta_4
    ta.right = ta_5
    ta_4.left = ta_1
    ta_4.right = ta_2

    tb = TreeNode(4)
    tb_1 = TreeNode(1)
    tb.left = tb_1

    res = Solution().mirrorTree(ta)
    print(res)
