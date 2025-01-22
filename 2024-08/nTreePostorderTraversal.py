# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: Node) -> List[int]:
        def helper(node, postorder):
            if not node:
                return node.val
            for c in node.children:
                helper(c, postorder)
            postorder.append(node.val)
            return postorder
        return helper(root, [])
            