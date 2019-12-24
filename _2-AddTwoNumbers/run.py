from AddTwoNumbers import ListNode, Solution

def arrToList(a, b):
    l1 = ListNode(a[0])
    l2 = ListNode(b[0])
    t1 = l1
    t2 = l2

    for i in range(1, len(a)):
        t1.next = ListNode(a[i])
        t2.next = ListNode(b[i])
        t1 = t1.next
        t2 = t2.next

    t1.next = None
    t2.next = None

    return l1, l2

if __name__ == '__main__':

    a = [2,4,3]
    b = [5,6,4]

    l1, l2 = arrToList(a, b)

    s = Solution()
    t = s.addTwoNumbers(l1, l2)

    while t:
        print(t.val, end=" ")
        t = t.next


