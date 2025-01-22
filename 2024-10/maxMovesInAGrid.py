from typing import List


def maxMoves(grid: List[List[int]]) -> int:
    n = len(grid)
    l = len(grid[0])
    memo = {}
    def helper(r: int, c: int, memo: dict, distance: int):
        if (r,c) in memo:
            return memo[(r,c)]
        if c == l-1:
            return distance
        # check possible moves
        k = grid[r][c]
        moves = []
        # up forward
        if r-1 >= 0:
            if grid[r-1][c+1] > k:
                moves.append((r-1,c+1))
        # forward
        if grid[r][c+1] > k:
            moves.append((r,c+1))
        # down forward
        if r+1 < l:
            if grid[r+1][c+1] > k:
                moves.append((r+1,c+1))
        if not moves:
            memo[(r,c)] = distance
        else:
            memo[(r,c)] = max([helper(i,j,memo,distance+1) for i,j in moves])
        return memo[(r,c)]
    max_moves = 0
    for i in range(n):
        max_moves = max(max_moves, helper(i,0,memo,0))
    return max_moves

print(maxMoves([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]))
        
        
