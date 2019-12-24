'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
'''
'''
这个题很简单  设置三个指针去维护链表就OK
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        headNode = ListNode(0)
        headNode.next = head
        p = headNode
        q = headNode.next
        if q:
            r = q.next

        while q and r:
            q.next = r.next
            r.next = q
            p.next = r

            p = q
            q = q.next
            if q:
                r = q.next

        return  headNode.next

import random
def createRandomList( n):
    if n <= 0:
        return None
    head = ListNode(random.randint(1, 20))
    p = head
    for i in range(n-1):
        q = ListNode(random.randint(1, 20))
        p.next = q
        p = p.next
    p.next = None
    return head

def printList( head):
    if head == None:
        return None
    p = head
    while p != None:
        print(p.val, end=' ')
        p = p.next



head = createRandomList(0)
printList(head)
print()

s = Solution()
headswap = s.swapPairs(head)
printList(headswap)