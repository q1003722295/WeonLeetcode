'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
'''
'''
这个题其实也不难，思路先遍历一遍链表确定个数 然后整除k就是需要翻转的次数
添加尾指针起始点为头结点  每次翻转都将尾指针记录下来 从尾指针起始进行头插法
然后将剩余链表插入新链表后面即可
'''


import random
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # n记录链表长度
        n = 0
        headNode = ListNode(0)#增加头结点
        headNode.next = head
        p = headNode
        while p.next:#计算链表长度
            n+=1
            p = p.next
        if n < k or (k == 0 or k == 1):#不足k个 直接返回
            return headNode.next

        # 增加新节点进行头插法 也就是翻转
        resNode = ListNode(0)
        resNode.next = None
        rear = resNode#每次都记录尾指针
        # 翻转的次数
        times = n // k

        # 头插法 每次从rear开始插入  进行times次
        for t in range(times):
            for i in range(k):
                # if p.next == None:
                #     break
                p = headNode.next
                headNode.next = p.next
                p.next = rear.next
                rear.next = p
                # 固定尾指针
                if i ==0:
                    reartemp = p
                if i == k-1:
                    rear = reartemp

        rear.next = headNode.next

        return resNode.next


# 随机生成长度为n的链表
def createRandomList( n):
    if n <= 0:
        return None
    head = ListNode(random.randint(1, 20))
    p = head
    for i in range(n - 1):
        q = ListNode(random.randint(1, 20))
        p.next = q
        p = p.next
    p.next = None
    return head

#打印链表
def printList( head):
    if head == None:
        return None
    p = head
    while p != None:
        print(p.val, end=' ')
        p = p.next

    print()


s = Solution()
l = createRandomList(12)
printList(l)
rl = s.reverseKGroup(l, 12)
printList(rl)
