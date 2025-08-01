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
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    while True:
        kth = prev
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next
        nxt = kth.next
        start = prev.next
        prev.next = reverseSegment(start, nxt)
        start.next = nxt
        prev = start


def linkedList(iterator):
    dummy = ListNode(0)
    cur = dummy
    for val in iterator:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next


a = linkedList(map(int, input("Enter list values: ").split()))
k = int(input("Enter k: "))
head = func(a, k)

print("Result:", end=" ")
cur = head
first = True
while cur:
    if not first:
        print("", end=" ")
    print(cur.val, end="")
    first = False
    cur = cur.next
print()

