class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def balanceBST(root: TreeNode) -> TreeNode:
        if root is None:
            return root
        nodes = []

        def traversal(node):
            if node:
                traversal(node.left)
                nodes.append(node)
                traversal(node.right)
        traversal(root)
        def balance(nodes, start, end):
            if start > end:
                return None

            # start, end = 0, len(nodes - 1)
            mid = (start+end) // 2
            node = nodes[mid]

            node.left = balance(nodes, start, mid - 1)
            node.right = balance(nodes, mid + 1, end)
            return node
        return balance(nodes, 0, len(nodes)-1)

      
      
      
        
