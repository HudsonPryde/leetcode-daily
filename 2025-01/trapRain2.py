from typing import List
from heapq import heappush, heappop


def trapRainWater(heightMap: List[List[int]]) -> int:
    n, m = len(heightMap), len(heightMap[0])
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    visited = set()
    q = []
    res = 0
    # create initial boundary
    for i in range(m):
        heappush(q, (heightMap[0][i], (0,i)))
        heappush(q, (heightMap[n-1][i], (n-1,i)))
        visited.update(set([(0,i), (n-1,i)]))
    for i in range(1,n-1):
        heappush(q, (heightMap[i][0], (i,0)))
        heappush(q, (heightMap[i][m-1], (i,m-1)))
        visited.update(set([(i,0), (i,m-1)]))
    while q:
        c_h,c= heappop(q)
        c_i,c_j = c
        for d_i,d_j in dirs:
            n_i,n_j = c_i+d_i,c_j+d_j
            if not (0 <= n_i < n) or not (0 <= n_j < m): continue
            if (n_i,n_j) in visited: continue
            n_h = heightMap[n_i][n_j]
            visited.add((n_i,n_j))
            if n_h >= c_h:
                heappush(q, (n_h,(n_i,n_j)))
            else:
                res += c_h - n_h
                heappush(q, (c_h,(n_i,n_j)))
    return res

print(trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]))