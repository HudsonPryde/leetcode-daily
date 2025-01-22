from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0
        def dfs(node):
            if not node:
                return defaultdict(int)
            if not node.left and not node.right:
                return defaultdict(int, {1: 1})

            left_depths = dfs(node.left)
            right_depths = dfs(node.right)

            # Count valid pairs
            for left in left_depths:
                for right in right_depths:
                    if left + right <= distance:
                        self.result += left_depths[left] * right_depths[right]

            # Update current distances
            current = defaultdict(int)
            for left in left_depths:
                if left + 1 <= distance:
                    current[left + 1] += left_depths[left]
            for right in right_depths:
                if right + 1 <= distance:
                    current[right + 1] += right_depths[right]

            return current

        dfs(root)
        return self.result


        