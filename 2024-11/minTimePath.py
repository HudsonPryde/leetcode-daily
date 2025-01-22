from typing import List
from heapq import heappush, heappop


def minimumTime(grid: List[List[int]]) -> int:
    n = len(grid)
    m = len(grid[0])
    #  nowhere to move from origin return -1
    if grid[0][1] > 1 and grid[1][0] > 1: return -1
    candidates = [(0, (0,0))]
    visited = set([(0,0)])
    while candidates:
        t, pos = heappop(candidates)
        # check all neighbours
        dirs = [(-1, 0),(0, -1),(1, 0),(0, 1)] # up, left, down, right
        for d1,d2 in dirs:
            # get new pos cords
            r, c = pos[0]+d1, pos[1]+d2
            # dont return to visited nodes
            if (r,c) in visited: continue
            # check if new pos is in grid boundary
            if 0 > r or r >= n or c < 0 or c >= m: continue
            # if node value is lower than current time+1 then set t for that node to t+1
            v = grid[r][c]
            new_t = -1
            if v <= t+1:
                new_t = t+1
            else:
                # if not add the node pos with a value of the time it would take occilating between a neighbour to move to the node
                # if curr t and node v remainder is the same we can waste the exact amount of time required
                if (v-t)%2 == 1:
                    new_t = v
                # otherwise v+1
                else:
                    new_t = v+1
            heappush(candidates, (new_t, (r,c)))
            # if node is end corner return it
            if r == n-1 and c == m-1: return new_t
            # mark visited
            visited.add((r,c))
    return -1

print(minimumTime([[0,5,1], [0,7,6],[7,7,1]]))
"""
0   2   4
0   5   5
5   4   3
"""