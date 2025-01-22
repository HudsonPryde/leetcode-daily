from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def replaceValueInTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    m = {}
    def levelSum(node: Optional[TreeNode], m: dict, d:int):
        if not node:
            return
        m[d] = m.get(d, 0) + node.val
        levelSum(node.left, m, d+1)
        levelSum(node.right, m, d+1)
    levelSum(root, m, 0)
    root.val = 0
    def solve(node: Optional[TreeNode], m: dict, d:int):
        if not node:
            return
        siblingSum = 0
        if node.left:
            siblingSum += node.left.val
        if node.right:
            siblingSum += node.right.val
        
        if node.left:
            node.left.val = m[d+1]-siblingSum
        if  node.right:
            node.right.val = m[d+1]-siblingSum
        solve(node.left, m, d+1)
        solve(node.right, m, d+1)
    solve(root, m, 0)
    return root

replaceValueInTree(TreeNode(5,TreeNode(4, TreeNode(1), TreeNode(10)),TreeNode(9,None,TreeNode(7))))