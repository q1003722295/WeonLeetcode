'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

'''

'''
简单的链表操作
'''
import random


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1

        head = ListNode(0)
        p = l1
        q = l2
        r = head
        while p != None and q != None:
            if p.val < q.val:
                r.next = p
                p = p.next
            else:
                r.next = q
                q = q.next

            r = r.next
        if p == None:
            r.next = q
        else:
            r.next = p


        return head.next

    def createListNode(self, n):
        temparr = []
        for i in range(n):
            temparr.append(random.randint(0, 20))

        temparr.sort()
        head = ListNode(0)
        p = head
        for i in range(n):
            p.next = ListNode(temparr[i])
            p = p.next

        p.next = None

        return head.next

    def printListNode(self, l):
        p = l
        while p != None:
            print(p.val, end=' ')
            p = p.next

        print()


s = Solution()
l1 = s.createListNode(10)
l2 = s.createListNode(0)
s.printListNode(l1)
s.printListNode(l2)
l = s.mergeTwoLists(l1, l2)

s.printListNode(l)
