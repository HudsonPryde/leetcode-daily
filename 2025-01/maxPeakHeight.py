from typing import List
from collections import deque

def highestPeak(isWater: List[List[int]]) -> List[List[int]]:
    n, m = len(isWater), len(isWater[0])
    q = deque()
    for i in range(n):
        for j in range(m):
            if isWater[i][j]:
                q.append((i,j))
                isWater[i][j] = 0
            else:
                isWater[i][j] = -1
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    
    while q:
        i,j = q.popleft()
        h = isWater[i][j]
        for d in dirs:
            n_i,n_j = i+d[0],j+d[1]
            if not (0 <= n_i < n) or not (0 <= n_j < m): continue
            if isWater[n_i][n_j] != -1: continue
            q.append((n_i,n_j))
            isWater[n_i][n_j] = h+1
    return isWater

print(highestPeak([[0,1],[0,0]]))

