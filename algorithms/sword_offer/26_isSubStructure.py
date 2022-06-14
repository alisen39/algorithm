#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/6/13 21:35
# desc:

""" 剑指 Offer 26. 树的子结构
https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof/
"""
'''
对称性递归。 烧脑~
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def is_sub(A, B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return is_sub(A.left, B.left) and is_sub(A.right, B.right)

        return bool(A and B) and (is_sub(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))


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

    res = Solution().isSubStructure(ta, tb)
    print(res)
