from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def delNodes(root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
    to_delete = set(to_delete)
    def find(node: Optional[TreeNode], prev: Optional[TreeNode], roots: List[TreeNode]):
        # end of tree return
        if not node:
            return None
        if node.val not in to_delete:
            if prev is None:
                roots.append(node)
            node.left = find(node.left, node, roots)
            node.right = find(node.right, node, roots)
            return node
        find(node.left, None, roots)
        find(node.right, None, roots)
        return None

    r = []
    find(root, None, r)
    return r
    
        