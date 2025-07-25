# Q9
# Solution in O(n) time and O(1) space

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseSegment(l: ListNode, r: ListNode) -> ListNode:
    prev = None
    cur = l
    while cur != r:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev

def func(head: ListNode, k: int) -> ListNode:
    tmp = ListNode(0)
    tmp.next = head
    prev = tmp
    while True:
        kth = prev
        for _ in range(k):
            kth = kth.next
            if not kth:
                return tmp.next
        nxt = kth.next
        start = prev.next
        prev.next = reverseSegment(start, nxt)
        start.next = nxt
        prev = start

def linkedList(a):
    tmp = ListNode(0)
    cur = tmp
    for val in a:
        cur.next = ListNode(val)
        cur = cur.next
    return tmp.next

try:
    a = list(map(int, input("Enter list values: ").split()))
    k = int(input("Enter k: "))
    if not 1 <= k <= len(a):
        print("Invalid input! k must be between 1 and length of list.")
        exit()
    head = func(linkedList(a), k)
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print("Result: ", result)
except ValueError:
    print("Invalid input!")
    exit()

