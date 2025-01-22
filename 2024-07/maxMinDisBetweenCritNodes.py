from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nodesBetweenCriticalPoints(head: Optional[ListNode]) -> List[int]:
    prev = head
    curr = head.next
    idx = 2
    firstc = None
    prevc = None
    currc = None
    mind = float('inf')
    while curr.next:
      if (curr.val < prev.val and curr.val < curr.next.val) or (curr.val > prev.val and curr.val > curr.next.val):
        if not prevc:
          firstc = idx
          prevc = idx
          currc = idx
        else:
          prevc = currc
          currc = idx
          mind = min(mind, currc-prevc)
      
      idx += 1
      curr = curr.next
      prev = prev.next
    if mind == float('inf'):
       return [-1,-1]
    return [mind, currc-firstc]


def createLinkedList(list):
  head = ListNode(0, None)
  curr = head
  for i, num in enumerate(list):
    curr.val = num
    if i < len(list)-1:
      curr.next = ListNode(0, None)
      curr = curr.next
  return head

print(nodesBetweenCriticalPoints(ListNode(3, ListNode(1, None))), " expect: [-1,-1]")
print(nodesBetweenCriticalPoints(createLinkedList([5,3,1,2,5,1,2])), " expect: [1,3]")
print(nodesBetweenCriticalPoints(createLinkedList([1,3,2,2,3,2,2,2,7])), " expect: [3,3]")
print(nodesBetweenCriticalPoints(createLinkedList([2,2,1,3])), " expect: [-1,-1]")
print(nodesBetweenCriticalPoints(createLinkedList([6,8,4,1,9,6,6,10,6])), " expect: [1,6]")