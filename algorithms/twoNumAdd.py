# 两数相加


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_add = 0
        l2_add = 0
        for index, num in l1:
            l1_add += num * (10 ** index)
        for index, num in l2:
            l2_add += num * (10 ** index)

        lsum = l1_add+l2_add

        return [int(x) for x in str(lsum)].reverse()


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    Solution().addTwoNumbers(l1, l2)
