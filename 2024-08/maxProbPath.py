from heapq import heapify, heappop, heappush
from typing import List


def maxProbability(n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
    visited = [0]*n
    adj = {x: [] for x in range(n)}
    for i, e in enumerate(edges):
        adj[e[0]].append((e[1],succProb[i]))
        adj[e[1]].append((e[0],succProb[i]))
    print(adj)
    prev = [None]*n
    dist = [float('-inf')]*n
    dist[start_node] = 1
    heap = [(0, start_node)]
    
    while heap:
        _, u= heappop(heap)
        for v, w in adj[u]:
            visited[u] = 1
            if dist[u] * w > dist[v]:
                prev[v] = u
                dist[v] = dist[u] * w
                if not visited[v]:
                    heappush(heap, (-(dist[u] * w), v))
    if dist[end_node] == float('-inf'):
        return 0
    return dist[end_node]

print(maxProbability(10, [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 5], [5, 6], [5, 7], [6, 8], [7, 9]], [0.1, 0.2, 0.5, 0.6, 0.3, 0.7, 0.8, 0.9, 0.4, 0.5], 0, 9))