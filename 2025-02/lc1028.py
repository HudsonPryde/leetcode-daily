from typing import Optional
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recoverFromPreorder(traversal: str) -> Optional[TreeNode]:
    depths = defaultdict(list)
    root = ''
    i=0
    for l in traversal:
        if l == '-': break
        root+=l
        i+=1
    depths[0].append(TreeNode(int(root)))
    dashes = 0
    digits = ''
    for l in traversal[i:]+'-':
        if l.isdigit():
            digits+=l
        elif l == '-' and digits:
            if not depths[dashes-1][-1].left:
                depths[dashes-1][-1].left = TreeNode(int(digits))
                depths[dashes].append(depths[dashes-1][-1].left)
            else:
                depths[dashes-1][-1].right = TreeNode(int(digits))
                depths[dashes].append(depths[dashes-1][-1].right)
            digits = ''
            dashes = 1
        else:
            dashes+=1
    return depths[0][0]
print(recoverFromPreorder("3"))