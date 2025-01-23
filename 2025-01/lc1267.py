from typing import List


def countServers(grid: List[List[int]]) -> int:
    n,m = len(grid), len(grid[0])
    rows, cols = [0]*n, [0]*m
    res = 0
    servers = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0: continue
            rows[i] += 1
            cols[j] += 1
            servers.append((i,j))
    for i,j in servers:
        if rows[i] > 1 or cols[j] > 1: res += 1
    return res

print(countServers([[1,0],[0,1]]))