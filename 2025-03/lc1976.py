from typing import List
from heapq import heappop,heappush
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 1_000_000_007
        adj = [[] for _ in range(n)]
        for u,v,w in roads:
            adj[u].append((v,w))
            adj[v].append((u,w))
        d = []
        min_lens = [float('inf')]*n
        p = [0]*n
        min_lens[0] = 0
        p[0] = 1
        heappush(d, (0,0))
        while d:
            time,node = heappop(d)
            if time > min_lens[node]:
                continue
            for v,w in adj[node]:
                if w+time < min_lens[v]:
                    min_lens[v] = w+time
                    p[v] = p[node]
                    heappush(d,(min_lens[v],v))
                elif w+time == min_lens[v]:
                    p[v] = (p[v] + p[node])%MOD
        return p[-1]

    
s = Solution()
print(s.countPaths(7,[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))

