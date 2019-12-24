# Definition for singly-linked list.

'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
'''


# 链表逐位相加 进的位记得加上去即可
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    def addTwoNumbers(self, l1, l2):

        num = l1.val + l2.val
        t = ListNode(num % 10)
        tempa = num // 10
        t.next = None
        tt = t
        l1 = l1.next
        l2 = l2.next

        while l1 is not None and l2 is not None:
            num = l1.val + l2.val + tempa
            tt.next = ListNode(num % 10)
            tempa = num // 10
            l1 = l1.next
            l2 = l2.next
            tt = tt.next

        if l1 == None:
            while l2 is not None:
                num = l2.val + tempa
                tt.next = ListNode(num % 10)
                tempa = num // 10
                tt = tt.next
                l2 = l2.next

        if l2 == None:
            while l1 is not None:
                num = l1.val + tempa
                tt.next = ListNode(num % 10)
                tempa = num // 10
                tt = tt.next
                l1 = l1.next

        if tempa: #如果最后还有多出的一位加上去
            tt.next = ListNode(tempa)
            tt.next.next = None

        return t






