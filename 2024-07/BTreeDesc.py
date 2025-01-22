
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createBinaryTree(descriptions: List[List[int]]) -> Optional[TreeNode]:
    d = {}
    children = set()
    for parent, child, isLeft in descriptions:
        children.add(child)
        node = TreeNode(child) if child not in d else d[child]

        if parent not in d:
            d[parent] = TreeNode(parent)

        if isLeft:
            d[child] = d[parent].left = node
        else:
            d[child] = d[parent].right = node 
        
    for node in d.keys():
        if node not in children:
            return d[node]
    

print(createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]))