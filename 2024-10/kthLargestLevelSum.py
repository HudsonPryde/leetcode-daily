from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthLargestLevelSum(root: Optional[TreeNode], k: int) -> int:
    m = {}
    def helper(node: Optional[TreeNode], m: dict, d: int):
        if not node: return
        m[d] = m.get(d, 0) + node.val
        helper(node.right, m, d+1)
        helper(node.left, m, d+1)
    helper(root, m, 0)
    if len(m.values()) < k: return -1
    return sorted(m.values(), reverse=True)[k-1]