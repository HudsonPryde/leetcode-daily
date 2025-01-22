from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
def mergeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
    total = 0
    merged = ListNode(0, None)
    currentNode = merged
    while head.next:
        print(head.next.val)
        if head.next.val == 0:
          currentNode.val = total
          print(currentNode.val)
          if head.next.next:
            currentNode.next = ListNode(0, None)
            currentNode = currentNode.next
            total = 0
        total += head.next.val
        head = head.next
    return merged

merged = mergeNodes(ListNode(0, ListNode(2, ListNode(3, ListNode(0, None)))))
while merged:
   print(merged.val)
   merged = merged.next