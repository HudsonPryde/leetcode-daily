from typing import List
from heapq import heappush, heappop


def minimumObstacles(grid: List[List[int]]) -> int:
    n = len(grid)
    m = len(grid[0])
    # modified djiksta each cell is a node with edges to 4 adj cells cells have costs of 0 or 1
    # return min cost route
    candidates = [(grid[0][0], (0,0))]
    visited = set()
    while candidates:
        # get the cand with curr smallest obstacles
        curr_v, curr_node = heappop(candidates)
        # add neighbours to candidates
        dirs = [(-1, 0),(0, -1),(1, 0),(0, 1)] # up, left, down, right
        for d1,d2 in dirs:
            # get new pos cords
            r, c = curr_node[0]+d1, curr_node[1]+d2
            # dont return to visited nodes
            if (r,c) in visited: continue
            # check if new pos is in grid boundary
            if 0 > r or r >= n or c < 0 or c >= m: continue
            # calc obstacle count for this node
            v = grid[r][c] + curr_v
            # if node is end corner return it
            if r == n-1 and c == m-1: return v
            # add it to the heap
            heappush(candidates, (v, (r,c)))
            # mark visited
            visited.add((r,c))

    return 0

print(minimumObstacles([[0,1,1],[1,1,0],[1,1,0]]))