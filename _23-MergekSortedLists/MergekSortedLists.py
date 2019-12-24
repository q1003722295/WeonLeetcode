'''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

'''



'''
使用优先队列 也就是堆排序

自己实现的堆排序

'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n = len(lists)
        lasthead = ListNode(0)
        plh = lasthead
        p = [ListNode(0)] * n
        valueindexs = [0] * n

        i=0
        j=0
        while j<n:
            if lists[j] == None:
                j+=1
                continue
            p[i] = lists[j]
            valueindexs[i] = i
            i+=1
            j+=1

        n = i

        def swap(a, b):
            t = a
            a = b
            b = t

            return a, b

        def adjustdown(valueindexs, start, end):
            dad = start
            j = dad * 2 + 1
            while j < n:
                if j+1 < n and p[valueindexs[j]].val > p[valueindexs[j+1]].val:
                    j+=1

                if p[valueindexs[dad]].val < p[valueindexs[j]].val:
                    break

                valueindexs[dad], valueindexs[j] = swap(valueindexs[dad], valueindexs[j])
                dad = j
                j = dad * 2 + 1

            return valueindexs

        for i in range(n // 2 - 1, -1, -1):
            adjustdown(valueindexs, i, n)

        while n != 0:
            valueindexs = adjustdown(valueindexs, 0, n)
            plh.next = p[valueindexs[0]]
            plh = plh.next

            if p[valueindexs[0]].next != None:
                p[valueindexs[0]] = p[valueindexs[0]].next
            else:
                valueindexs[0], valueindexs[n - 1] = swap(valueindexs[0], valueindexs[n-1])
                n = n-1

        plh.next = None
        return lasthead.next



def arrytoNodelist(arr):
    head = ListNode(0)
    p = head
    for i in range(len(arr)):
        p.next = ListNode(arr[i])
        p = p.next

    p.next = None
    return head.next


s = Solution()
a = [[7],[6,42],[3,5],[4,8]]
lists = [arrytoNodelist(a[0]),arrytoNodelist(a[1]), arrytoNodelist(a[2]), arrytoNodelist(a[3])]
lasthead = s.mergeKLists(lists)
p = lasthead
while(p):
    print(p.val)
    p = p.next


