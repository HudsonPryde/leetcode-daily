# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0
        self.elements = set()
        self.recover(self.root)
    
    def recover(self, node: Optional[TreeNode]):
        self.elements.add(node.val)
        if node.left:
            node.left.val = 2*node.val+1
            self.recover(node.left)
        if node.right:
            node.right.val = 2*node.val+2
            self.recover(node.right)

    def find(self, target: int) -> bool:
        return target in self.elements


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)