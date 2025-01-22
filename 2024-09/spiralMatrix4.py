from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def spiralMatrix(m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
    res = [[-1 for _ in range(n)] for _ in range(m)]
    pos = [0,0]
    visited = set()
    d = 0
    curr = head
    while curr:
        res[pos[0]][pos[1]] = curr.val
        visited.add((pos[0],pos[1]))
        if not curr.next:
            break
        if d%4 == 0:
            if (pos[0],pos[1]+1) in visited or pos[1]+1 >= n:
                d += 1
                continue
            pos[1] += 1
        elif d%4 == 1:
            if (pos[0]+1,pos[1]) in visited or pos[0]+1 >= m:
                d += 1
                continue
            pos[0] += 1
        elif d%4 == 2:
            if (pos[0],pos[1]-1) in visited or pos[1]-1 < 0:
                d += 1
                continue
            pos[1] -= 1
        elif d%4 == 3:
            if (pos[0]-1,pos[1]) in visited or pos[0]-1 < 0:
                d += 1
                continue
            pos[0] -= 1
        
        curr = curr.next
    return res

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
h = ListNode(l[0])
c = h
for n in l[1:]:
    c.next = ListNode(n)
    c = c.next
print(spiralMatrix(4,4,h))