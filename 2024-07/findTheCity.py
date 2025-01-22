from heapq import heappop, heappush
from typing import List


def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    # edges[i] = [from_i, to_i, weight_i]
    neighbors = [[] for _ in range(n)]
    for f, t, w in edges:
        neighbors[f].append((t, w))
        neighbors[t].append((f, w))

    def dijkstra(source: int):
        dist = [float('inf') for _ in range(n)]
        prev = [False for _ in range(n)]
        count = 0
        dist[source] = 0
        heap = [(0,source)]
        while heap and count < n:
            u, id = heappop(heap)
            if prev[id]: continue
            prev[id] = True
            for city, w in neighbors[id]:
                if u+w < dist[city]:
                    dist[city] = u+w
                    heappush(heap, (u+w, city))
        return len([ d for d in dist if 0<d<=distanceThreshold])
    res, cur_min = None, float('inf')
    for i in range(n):
        v = dijkstra(i)
        if v <= cur_min:
            res = i
            cur_min = v
    return res

print(findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4))