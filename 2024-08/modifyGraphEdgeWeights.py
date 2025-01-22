from heapq import heappop, heappush
from typing import List


def modifiedGraphEdges(n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
    adj = {x:[] for x in range(n)}
    wild_edges = []
    for i,e in enumerate(edges):
        a,b,w = e
        if w > 0:
            adj[a].append((w,b))
            adj[b].append((w,a))
        else:
            wild_edges.append(i)
    
    def dijkstra():
        dist = [float('inf')]*n
        dist[source] = 0

        q = [(0, source)]

        while q:
            d, u = heappop(q)
            if u == destination:
                return d
            for v, w in adj[u]:
                alt = d + w
                if alt < dist[v]:
                    dist[v] = alt
                    heappush(q, (alt, v))
        return float('inf')
    
    dist = dijkstra()
    if dist < target: return []

    for i in wild_edges:
        edges[i][2]=target+1
    if dist==target: return edges

    for i in wild_edges:
        new_edge = edges[i]
        u,v = new_edge[0],new_edge[1]
        new_edge[2] = 1
        adj[u].append((1,v))
        adj[v].append((1,u))
        dist = dijkstra()
        if dist<=target:
            new_edge[2]+=target-dist
            return edges

    return []

print(modifiedGraphEdges(5, [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], 0, 1, 5))