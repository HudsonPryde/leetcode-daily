from typing import Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def reverseOddLevels(root: Optional[TreeNode]) -> Optional[TreeNode]:
    d = defaultdict(list)
    def search(node, d, depth):
        if not node:
            return
        if depth%2 == 1:
            d[depth].append(node.val)
        search(node.left, d, depth+1)
        search(node.right,d,depth+1)
    search(root, d, 0)
    idx = defaultdict(int)
    def helper(node, d, depth, idx):
        if not node:
            return
        if depth%2 == 1:
            node.val = d[depth][len(d[depth])-idx[depth]]
            idx[depth] += 1
        helper(node.left, d, depth+1, idx)
        helper(node.right,d,depth+1, idx)
    helper(root, d, 0, idx)
    return root