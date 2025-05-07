from heapq import heappush, heappop
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n,m = len(moveTime),len(moveTime[0])
        q = [(0,(0,0))]
        seen = set()
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        while q:
            t, pos = heappop(q)
            if pos == (n-1,m-1):
                return t
            for u,v in dirs:
                p = (pos[0]+u,pos[1]+v)
                if not (0 <= p[0] < n) or not (0 <= p[1] < m): continue
                if p not in seen:
                    heappush(q, (max(t+1,moveTime[p[0]][p[1]]+1), p))
                    seen.add(p)
        return -1
s = Solution()
print(s.minTimeToReach([[0,1],[1,2]]))
            

