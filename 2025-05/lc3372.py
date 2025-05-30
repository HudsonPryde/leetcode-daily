from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        if k == 0:
            return [1]*(len(edges1)+1)
        adj1, adj2 = {}, {}
        for u,v in edges1:
            adj1[u] = adj1.get(u,[]) + [v]
            adj1[v] = adj1.get(v,[]) + [u]
        for u,v in edges2:
            adj2[u] = adj2.get(u,[]) + [v]
            adj2[v] = adj2.get(v,[]) + [u]
        max_dist = 0
        for node in range(len(edges2)+1):
            max_dist = max(max_dist, self._helper(node,k-1,adj2,0,node))
        
        res = []
        for node in range(len(edges1)+1):
            res.append(self._helper(node,k,adj1,0,node)+max_dist)
        return res
    
    def _helper(self, node: int, k: int, adj: dict, dist: int, prev: int):
        if dist >= k:
            return 1
        t = 1
        for v in adj[node]:
            if v == prev: continue
            t += self._helper(v, k, adj, dist + 1, node)
        return t

s = Solution()
print(s.maxTargetNodes([[0,1]],[[0,1]], 0))