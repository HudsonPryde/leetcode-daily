# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root: return False

        stack = [(root, head)]

        while stack:
            node, lst = stack.pop()

            if not node:
                continue

            if self.helper(node, lst):
                return True
            
            if node.left:
                stack.append((node.left, head))
            if node.right:
                stack.append((node.right, head))
        return False
    
    def helper(self, node, lst):
        while node and lst:
            if node.val != lst.val:
                return False
            lst = lst.next
            if lst:
                node = node.left if node.left and self.helper(node.left, lst) else node.right
        return lst is None
s = Solution()

# print(s.isSubPath(ListNode(1, ListNode(10, None)), TreeNode(1, None, TreeNode(1, TreeNode(10, TreeNode(9, None)), TreeNode(1, None)))))
print(s.isSubPath(ListNode(2, ListNode(2, ListNode(1,None))), TreeNode(2, None, TreeNode(2, None, TreeNode(2, None, TreeNode(1, None))))))