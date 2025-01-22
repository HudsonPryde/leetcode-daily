from typing import List


def gameOfLife(board: List[List[int]]) -> None:
    r,c = len(board),len(board[0])
    alive = set()
    dead = set()
    def check_cell(x,y):
        up = (x,y-1)
        up_right = (x+1,y-1)
        up_left = (x-1,y-1)
        left = (x-1,y)
        right = (x+1,y)
        down = (x,y+1)
        down_right = (x+1,y+1)
        down_left = (x-1,y+1)
        live_neighbors = 0
        cells = [up,up_right,up_left,left,right,down,down_left,down_right]
        for i,j in cells:
            if 0<=j<r and 0<=i<c and board[j][i]:
                live_neighbors += 1
        if board[y][x] and live_neighbors < 2:
            dead.add((x,y))
            return
        if board[y][x] and 2 <= live_neighbors <= 3:
            alive.add((x,y))
            return
        if board[y][x] and live_neighbors > 3:
            dead.add((x,y))
            return
        if not board[y][x] and live_neighbors == 3:
            alive.add((x,y))
            return
    
    for i in range(r):
        for j in range(c):
            check_cell(j,i)
    for i in range(r):
        for j in range(c):
            if (j,i) in alive: board[i][j] = 1
            elif (j,i) in dead: board[i][j] = 0

