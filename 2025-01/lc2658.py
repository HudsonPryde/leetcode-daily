from typing import List


def findMaxFish(grid: List[List[int]]) -> int:
    m,n = len(grid),len(grid[0])

    def helper(i,j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
            return 0

        t = grid[i][j]
        grid[i][j] = 0

        return t + helper(i-1, j) + helper(i+1, j) + helper(i, j-1) + helper(i, j+1)
    
    res = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0: continue
            res = max(res, helper(i,j))
    return res

print(findMaxFish([[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]))