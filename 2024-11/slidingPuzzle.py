from typing import List
from collections import deque


def slidingPuzzle(board: List[List[int]]) -> int:
    for i in range(2):
        for j in range(3):
            if board[i][j] == 0:
                open_pos = (i,j)
    
    boards = set()
    def serialize(board: List[List[int]]):
            return (tuple(board[0][:]), tuple(board[1][:]))
    
    # heap for board configs to consider
    moves = deque([(0,board,open_pos,open_pos)])
    while moves:
        # get board config with smallest move
        num_moves, b, pos, last_pos = moves.popleft()
        if b == [[1,2,3],[4,5,0]]:
            return num_moves
        
        # check for a loop
        b_rep = serialize(b)
        if b_rep in boards:
            continue
        boards.add(b_rep)
        # dont undo last move
        new_pos = (pos[0]+1, pos[1]) # down 1
        if new_pos[0] < 2 and new_pos != last_pos:
            new_b = [b[0][:], b[1][:]]
            num = new_b[new_pos[0]][new_pos[1]]
            new_b[new_pos[0]][new_pos[1]] = 0
            new_b[pos[0]][pos[1]] = num
            moves.append((num_moves+1, new_b, new_pos, pos))
        
        new_pos = (pos[0]-1, pos[1]) # up 1
        if new_pos[0] >= 0 and new_pos != last_pos:
            new_b = [b[0][:], b[1][:]]
            num = new_b[new_pos[0]][new_pos[1]]
            new_b[new_pos[0]][new_pos[1]] = 0
            new_b[pos[0]][pos[1]] = num
            moves.append((num_moves+1, new_b, new_pos, pos))
        
        new_pos = (pos[0], pos[1]+1) # right 1
        if new_pos[1] < 3 and new_pos != last_pos:
            new_b = [b[0][:], b[1][:]]
            num = new_b[new_pos[0]][new_pos[1]]
            new_b[new_pos[0]][new_pos[1]] = 0
            new_b[pos[0]][pos[1]] = num
            moves.append((num_moves+1, new_b, new_pos, pos))
        
        new_pos = (pos[0], pos[1]-1) # left 1
        if new_pos[1] >= 0 and new_pos != last_pos:
            new_b = [b[0][:], b[1][:]]
            num = new_b[new_pos[0]][new_pos[1]]
            new_b[new_pos[0]][new_pos[1]] = 0
            new_b[pos[0]][pos[1]] = num
            moves.append((num_moves+1, new_b, new_pos, pos))

print(slidingPuzzle([[1,2,3],[4,0,5]]))