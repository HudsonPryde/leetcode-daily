# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self._helper(root,0)[0]
    def _helper(self,node,depth):
        if not node:
            return (node,0)
        if not node.left and not node.right:
            return (node, depth)
        l_parent,l_depth = self._helper(node.left,depth+1)
        r_parent,r_depth = self._helper(node.right,depth+1)
        if l_depth == r_depth:
            return (node,r_depth)
        elif l_depth > r_depth:
            return (l_parent,l_depth)
        else:
            return (r_parent,r_depth)

