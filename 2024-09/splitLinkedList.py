from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def splitListToParts(head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    n = 0
    curr = head
    while curr:
        n += 1
        curr = curr.next
    
    if k >= n:
        d, r = 1, 0
    else:
        d, r = n // k, n%k
    res = []

    curr = head
    i = 1
    while curr:
        if i == 1:
            res.append(curr)
        if i == d and r > 0:
            r -= 1
        elif i >= d:
            i = 1
            temp = curr.next
            curr.next = None
            curr = temp
            continue
        i += 1
        curr = curr.next
    res.extend([[] for _ in range(k-len(res))])
    return res

print(splitListToParts(ListNode(1,ListNode(2,ListNode(3,None))), 5))