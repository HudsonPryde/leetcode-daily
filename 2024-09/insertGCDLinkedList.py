from typing import Optional
import math
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def insertGreatestCommonDivisors(head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    while curr.next:
        n = curr.next
        new = ListNode(math.gcd(n.val, curr.val), n)
        curr.next = new
        curr = n
    return head
l = [18,6,10,3]
h = ListNode(l[0])
c = h
for n in l[1:]:
    c.next = ListNode(n)
    c = c.next
insertGreatestCommonDivisors(h)