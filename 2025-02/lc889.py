from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.preindex = 0
        self.postindex = 0
    def constructFromPrePost(self,preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self._helper(preorder,postorder)
    def _helper(self,preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        node = TreeNode(preorder[self.preindex])
        self.preindex += 1

        if node.val != postorder[self.postindex]:
            node.left = self._helper(preorder,postorder)
        
        if node.val != postorder[self.postindex]:
            node.right = self._helper(preorder,postorder)
        
        self.postindex += 1
        return node

