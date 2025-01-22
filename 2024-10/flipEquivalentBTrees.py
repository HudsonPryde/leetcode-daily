from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flipEquiv(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    if root1 and not root2:
        return False
    if root2 and not root1:
        return False
    if root1 and root2 and root1.val != root2.val:
        return False
    if not root1 and not root2:
        return True
    m1 = {}
    m2 = {}
    def helper(node: Optional[TreeNode], m: dict):
        m[node.val] = []
        if node.left:
            m[node.val].append(node.left.val)
            helper(node.left, m)
        if node.right:
            m[node.val].append(node.right.val)
            helper(node.right, m)
    helper(root1, m1)
    helper(root2, m2)
    
    for k,v in m1.items():
        if set(v) != set(m2[k]):
            return False
    return True

print(flipEquiv(TreeNode(0, TreeNode(1, TreeNode(2, None, TreeNode(3)))), TreeNode(0, None, TreeNode(1, None, TreeNode(2, None, TreeNode(3))))))