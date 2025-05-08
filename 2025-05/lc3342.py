from heapq import heappush, heappop
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n,m = len(moveTime),len(moveTime[0])
        q = [(0,(0,0), 0)]
        seen = set()
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        while q:
            t, pos, b = heappop(q)
            if pos == (n-1,m-1):
                return t
            for u,v in dirs:
                p = (pos[0]+u,pos[1]+v)
                if not (0 <= p[0] < n) or not (0 <= p[1] < m): continue
                inc = 1 if not b else 2
                if p not in seen:
                    heappush(q, (max(t+inc,moveTime[p[0]][p[1]]+inc), p, not b))
                    seen.add(p)
        return -1
s = Solution()
print(s.minTimeToReach([[0,4],[4,4]]))
            

