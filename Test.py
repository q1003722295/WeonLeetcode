import random

# 链表的测试
#为了迎合leetcode 链表都不带头结点
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # 随机生成长度为n的链表
    def createRandomList(self, n):
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
    def printList(self, head):
        if head == None:
            return None
        p = head
        while p != None:
            print(p.val, end=' ')
            p = p.next

        print()

    #将数组转化为链表
    def arrytoNodelist(self, arr):
        head = ListNode(0)
        p = head
        for i in range(len(arr)):
            p.next = ListNode(arr[i])
            p = p.next

        p.next = None
        return head.next

class List(object):

    # 随机生成数组nums
    def CreateArr(self, n):
        arr = [0] * n
        for i in range(n):
            arr[i] = random.randint(-10, 10)
        return arr

    #打印数组
    def printArr(self, arr, n):
        for i in range(n):
            print(arr[i], end=' ')

        print()
