from typing import List
from collections import deque


def minCost(grid: List[List[int]]) -> int:
    n,m = len(grid), len(grid[0])
    visited = set()
    dir = [(0,1),(0,-1),(1,0),(-1,0)]
    q = deque([(0, (0,0))])
    while q:
        w, cords = q.popleft()
        r,c = cords
        if (r,c) in visited: continue
        visited.add((r,c))
        if (r,c) == (n-1,m-1):
            return w
        for i,d in enumerate(dir):
            dr,dc = d
            n_r,n_c = dr+r,dc+c
            if (0 <= n_r < n) and (0 <= n_c < m):
                if (n_r,n_c) in visited: continue
                if grid[r][c] == i+1:
                    q.appendleft((w, (n_r,n_c)))
                else:
                    q.append((w+1, (n_r,n_c)))
print(minCost([[1,1,3],[3,2,2],[1,1,4]]))
        

