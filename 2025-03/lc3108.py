from typing import List
from collections import deque
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        adj = {}
        for u,v,w in edges:
            adj[u] = adj.get(u,[]) + [(v,w)]
            adj[v] = adj.get(v,[]) + [(u,w)]
        idx = 0
        res = []
        res_map = {}
        for i in range(n):
            if i in res_map: continue
            if i not in adj:
                res_map[i] = idx
                res.append(-1)
                idx += 1
                continue
            d = deque([i])
            t = None
            seen = set()
            res_map[i] = idx
            while d:
                u = d.popleft()
                if u in seen: continue
                seen.add(u)
                for v,w in adj[u]:
                    if t == None:
                        t = w
                    else:
                        t = t&w
                    res_map[v] = idx
                    d.append(v)
            res.append(t)
            idx += 1
        return [ res[res_map[u]] if res_map[u] == res_map[v] else -1 for u,v in query ]

s = Solution()
print(s.minimumCost(3,[[0,2,7],[0,1,15],[1,2,6],[1,2,1]],[[1,2]]))
        