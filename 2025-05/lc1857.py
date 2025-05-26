from collections import deque
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        c_list = {x: i for i,x in enumerate(list(set(colors)))}
        m = len(c_list)
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)

        
        stack, visited = self._topo(adj)
        if visited != len(adj): return -1
        res = -1

        dp = [None for _ in range(n)]
        for i in stack:
            if dp[i] != None: continue
            f = self._helper(i,m,dp,adj,c_list,colors)
            if f == -1: return -1
            res = max(max(f),res)
        return res
    
    def _helper(self, node: int, m: int, dp: List[List[int]], adj: List[List[int]], c_list: dict, colors: List[str]):
        if dp[node] != None:
            return dp[node]

        dp[node] = [0]*m
        for i in adj[node]:
            f = self._helper(i,m,dp,adj,c_list,colors)
            for k in range(m):
                dp[node][k] = max(dp[node][k],f[k])

        dp[node][c_list[colors[node]]] += 1
        return dp[node]


    def _topo(self, adj:List[List[int]]):
        d = [0]*len(adj)
        q = deque()
        visited = 0
        for u in range(len(adj)):
            for v in adj[u]:
                d[v] += 1
        
        for u in range(len(adj)):
            if d[u] == 0:
                q.append(u)
        stack = []
        while q:
            u = q.popleft()
            stack.append(u)
            visited += 1
            for v in adj[u]:
                d[v] -= 1
                if d[v] == 0:
                    q.append(v)
        return stack, visited


s = Solution()
print(s.largestPathValue("ctlcw",[[1,0],[2,0],[3,0],[4,0]]))