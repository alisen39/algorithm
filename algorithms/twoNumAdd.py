# 两数相加


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        r = ListNode(0)

        # carry = 0
        # while l1 or l2:
        pass





        # i+=1



if __name__ == '__main__':
    l1 = ListNode(2)
    l2 = ListNode(4)
    l3 = ListNode(5)

    l1.next = l2
    l2.next = l3

    n1 = ListNode(5)
    n2 = ListNode(6)
    n3 = ListNode(4)
    n1.next = n2
    n2.next = n3

    res = Solution().addTwoNumbers(l1, n1)
    print(res)
    # l1 = [2, 4, 3]
    # l2 = [5, 6, 4]
    # Solution().addTwoNumbers(l1, l2)
