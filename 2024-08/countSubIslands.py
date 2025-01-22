from typing import List


def countSubIslands(grid1: List[List[int]], grid2: List[List[int]]) -> int:
    for row in grid1:
        print(row)
    print('\n')
    for row in grid2:
        print(row)
    def helper(i,j,grid,visited):
        n,k = len(grid), len(grid[0])
        neighbours = []
        # up i-1, j
        if i-1 >= 0 and (i-1,j) not in visited:
            if grid[i-1][j] == 1:
                neighbours.append((i-1,j))
        # down i+1, j
        if i+1 < n and (i+1,j) not in visited:
            if grid[i+1][j] == 1:
                neighbours.append((i+1,j))
        # left i, j-1
        if j-1 >= 0 and (i,j-1) not in visited:
            if grid[i][j-1]:
                neighbours.append((i,j-1))
        if j+1 < k and (i,j+1) not in visited:
            if grid[i][j+1]:
                neighbours.append((i,j+1))
        return neighbours

    res = 0
    visited2 = set()
    for i in range(len(grid2)):
        for j in range(len(grid2[i])):
            if (i,j) in visited2 or grid2[i][j] == 0 or grid1[i][j]==0:
                continue
            island = []
            neighbours = [(i,j)]
            if i == 2 and j > 10:
                print(neighbours)
            exited=0
            while neighbours:
                n = neighbours.pop()
                if grid1[n[0]][n[1]] == 0:
                    exited=1
                if n in visited2:
                    continue
                visited2.add(n)
                island.append(n)
                neighbours.extend(helper(n[0],n[1],grid2,visited2))

            if not exited:
                res += 1
            print(island, res)

    return res

print(countSubIslands([[1,0,1],[1,0,0],[0,1,1]], [[1,1,0],[1,0,0],[0,1,1]]))