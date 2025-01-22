from typing import List


def gridGame(grid: List[List[int]]) -> int:
    n = len(grid[0])
    row1 = sum(grid[0][1:])
    row2 = 0
    res = row1
    for i in range(n-1):
        # goal is to minimize the max route rob2 could take
        row1 -= grid[0][i+1]
        row2 += grid[1][i]
        dif = max(row1,row2)
        if dif <= res:
            res = dif
        else:
            break
    return res



print(gridGame([[3,3,21],[18,15,2]]))