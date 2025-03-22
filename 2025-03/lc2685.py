from typing import List
from collections import defaultdict

class UnionFind:
    def __init__(self,n):
        self.root = set([i for i in range(n)])
        self.parent = [-1]*n
        self.size = [1]*n
        self.edge = [0]*n
    def _find(self,node):
        if self.parent[node] == -1:
            return node
        self.parent[node] = self._find(self.parent[node])
        return self.parent[node]
    def _union(self,node_1,node_2):
        root_1 = self._find(node_1)
        root_2 = self._find(node_2)

        if root_1 == root_2:
            self.edge[root_1] += 1
            return
        
        min_root = min(root_1,root_2,key=lambda x: self.size[x])
        max_root = max(root_2,root_1,key=lambda x: self.size[x])
        self.parent[min_root] = max_root
        self.size[max_root] += self.size[min_root]
        if min_root in self.root: self.root.remove(min_root)
        self.edge[max_root] += self.edge[min_root] + 1

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        ds = UnionFind(n)
        for u,v in edges:
            ds._union(u,v)
            
        print(ds.root,ds.size,ds.parent,ds.edge)
        res = 0
        for i in list(ds.root):
            if ds.edge[i] == (ds.size[i]*(ds.size[i]-1))/2:
                res += 1
        return res




        
s = Solution()
print(s.countCompleteComponents(5,[[1,2],[3,4],[1,4],[2,3],[1,3],[2,4]]))