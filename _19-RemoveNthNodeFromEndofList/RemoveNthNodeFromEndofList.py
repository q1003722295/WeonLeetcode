'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

'''

'''
双指针法
上述算法可以优化为只使用一次遍历。我们可以使用两个指针而不是一个指针。第一个指针从列表的开头向前移动 n+1 步，
而第二个指针将从列表的开头出发。现在，这两个指针被 n 个结点分开。我们通过同时移动两个指针向前来保持这个恒定的间隔，
直到第一个指针到达最后一个结点。此时第二个指针将指向从最后一个结点数起的第 n 个结点。
我们重新链接第二个指针所引用的结点的 next 指针指向该结点的下下个结点。

最坑爹的是 leetcode上不给你安排头结点 你得自己先弄个头结点 返回首元结点！！
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0:
            return head

        virthead = ListNode(0)
        virthead.next = head
        p = virthead
        q = virthead
        t = n

        while t>0 and p.next:
            t -= 1
            p = p.next

        if p.next == None and t != 0:
            return None


        while p.next:
            p = p.next
            q = q.next
        q.next = q.next.next
        return virthead.next

import random
class Test(object):
    def createRandomList(self,n):
        head = ListNode(random.randint(1, 10))
        p = head
        for i in range(n-1):
            q = ListNode(random.randint(1, 10))
            p.next = q
            p = p.next
        p.next = None
        return head

    def printList(self, head):
        if head == None:
            return None
        p = head.next
        while p != None:
            print(p.val, end=' ')
            p = p.next


s = Solution()
t = Test()
for i in range( 13):
    head = t.createRandomList( 10)
    t.printList(head)
    print()
    print(i)

    h = s.removeNthFromEnd(head, i)
    t.printList(h)
    print()
    print()