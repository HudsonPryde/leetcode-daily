class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    def helper(node, order):
        if not node:
            return order
        if not node.left and not node.right:
            order.append(node.val)
            return order
        if node.left:
            order = helper(node.left, order)
        if node.right:
            order = helper(node.right, order)
        order.append(node.val)
        return order
    return helper(root, [])

print(postorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3, None), None))))