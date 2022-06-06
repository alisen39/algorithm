#!/usr/bin/env python
# encoding: utf-8
# author: Alisen
# time: 2022/6/6 16:44
# desc:
""" 剑指 Offer 32 - I. 从上到下打印二叉树
https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/
"""

from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        res = []
        if not root: return res
        queue = deque([])
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res


if __name__ == '__main__':
    t3 = TreeNode(3)
    t9 = TreeNode(9)
    t20 = TreeNode(20)
    t15 = TreeNode(15)
    t7 = TreeNode(7)
    t3.left = t9
    t3.right = t20
    t20.left = t15
    t20.right = t7
    res = Solution().levelOrder(t3)
    print(res)
