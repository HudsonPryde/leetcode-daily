
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

from typing import List

#each node has exactly four children
# 1. if cur grid all 1s or 0s set isLeaf true and set val to val of grid (1,0) children are nul
# 2. else isLeaf false val is any and children become the 4 quads of the grid
# 3. recurse children
class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        root = Node(True,False)
        self.getQuads(grid, root)
        self.printQuadTree(root)
        n = len(grid)
        print(grid[:n//2][:n//2])
        return root
    def getQuads(self, grid: List[List[int]], node: Node):
        n = len(grid)
        if n == 0: return
        # q1
        c1 = Node(grid[0][0]==1,True)
        for i in range(n//2):
            for j in range(n//2):
                if grid[i][j] != c1.val:
                    c1.isLeaf = False
                    self.getQuads(grid[:n//2][:n//2], c1)
                    break
            if not c1.isLeaf: break
        node.topLeft = c1
        # q2
        c2 = Node(grid[0][n//2]==1,True)
        for i in range(n//2):
            for j in range(n//2,n):
                if grid[i][j] != c2.val:
                    c2.isLeaf = False
                    self.getQuads(grid[:n//2][n//2:], c2)
                    break
            if not c2.isLeaf: break
        node.topRight = c2
        # q3
        c3 = Node(grid[n//2][0]==1,True)
        for i in range(n//2,n):
            for j in range(n//2):
                if grid[i][j] != c3.val:
                    c3.isLeaf = False
                    self.getQuads(grid[n//2:][:n//2], c3)
                    break
            if not c3.isLeaf: break
        node.bottomLeft = c3
        # q4
        c4 = Node(grid[n//2][n//2]==1,True)
        for i in range(n//2,n):
            for j in range(n//2,n):
                if grid[i][j] != c4.val:
                    c4.isLeaf = False
                    self.getQuads(grid[:n//2][:n//2], c4)
                    break
            if not c4.isLeaf: break
        node.bottomRight = c4
    def printQuadTree(self, node: Node):
        if not node: return
        print([node.isLeaf,node.val])
        self.printQuadTree(node.topLeft)
        self.printQuadTree(node.topRight)
        self.printQuadTree(node.bottomLeft)
        self.printQuadTree(node.bottomRight)

Solution().construct([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]])