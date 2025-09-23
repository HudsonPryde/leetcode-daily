from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set() # track seen grid cells
        dirs = [(0,1),(1,0),(-1,0),(0,-1)] # surrounding cells
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not (i,j) in seen:
                    q = deque([(i,j)])
                    seen.add((i,j))
                    while q:
                        a,b = q.popleft()
                        for x,y in dirs:
                            if (a+x,b+y) in seen: continue
                            if 0<=a+x<len(grid) and 0<=b+y<len(grid[0]) and grid[a+x][b+y] == "1":
                                q.append((a+x,b+y))
                                seen.add((a+x,b+y))
                    islands += 1
        return islands

