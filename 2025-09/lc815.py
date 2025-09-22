from typing import List
from collections import defaultdict, deque
# do not start on bus
# routes can be made into adj matrix
# djisktra to find shortest path
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        n = len(routes)
        stopToBus = defaultdict(list)
        for i in range(n):
            for s in routes[i]:
                stopToBus[s].append(i)
        seenStops = set([source])
        seenBuses = set()
        q = deque([(source,0)])
        while q:
            stop,steps = q.popleft()
            for b in stopToBus[stop]:
                if b in seenBuses: continue
                for s in routes[b]:
                    if s in seenStops: continue
                    if s == target: return steps+1
                    q.append((s,steps+1))
                    seenStops.add(s)
                seenBuses.add(b)
        return -1

print(Solution().numBusesToDestination([[1,2,7],[3,6,7]],1,6))