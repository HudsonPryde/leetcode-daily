from heapq import heappop, heappush
from typing import List


def minimumCost(source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
    INF = float('inf')
    n = 26
    dist = [[INF]*n for _ in range(n)]
    
    def convertChar(c: str) -> int:
        return ord(c) - ord('a')
    
    for h in range(n):
        dist[h][h] = 0
    
    for o,c,p in zip(original,changed,cost):
        dist[convertChar(o)][convertChar(c)] = min(p, dist[convertChar(o)][convertChar(c)])
    
    for k in range(n):
        for i in range(n):
            if dist[i][k] < INF:
                for j in range(n):
                    if dist[k][j] < INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    total = 0
    for s,t in zip(source,target):
        v = dist[convertChar(s)][convertChar(t)]
        if s != t:
            if v == INF:
                print(s, t)
                return -1
            else:
                total += v
    return total

print(minimumCost("aaadbdcdac", "cdbabaddba", ["a","c","b","d","b","a","c"], ["c","a","d","b","c","b","d"], [7,2,1,3,6,1,7]))