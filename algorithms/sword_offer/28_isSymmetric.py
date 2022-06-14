#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/6/13 21:35
# desc:
""" 剑指 Offer 28. 对称的二叉树
https://leetcode.cn/problems/dui-cheng-de-er-cha-shu-lcof/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True

        def recur(L, R):
            if not L and not R:
                return True

            if not L or not R or L.val != R.val:
                return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return recur(root.left, root.right)


if __name__ == '__main__':
    ta = TreeNode(3)
    ta_1_0 = TreeNode(1)
    ta_1_1 = TreeNode(2)
    ta.left = ta_1_0
    ta.right = ta_1_1
    res = Solution().isSymmetric(ta)
    print(res)
