from typing import List


def numMagicSquaresInside(grid: List[List[int]]) -> int:
    magic_squares = 0
    def checkSquare(i: int, j: int):
        row1 = set([grid[i][j+h] for h in range(3) if 0<grid[i][j+h]<=9])
        row2 = set([grid[i+1][j+h] for h in range(3) if 0<grid[i+1][j+h]<=9])
        row3 = set([grid[i+2][j+h] for h in range(3) if 0<grid[i+2][j+h]<=9])
        if (sum(row1) != sum(row2) != sum(row3)) or (len(row1) < 3 or len(row2) < 3 or len(row3) < 3):
            return False
        col1 = set([grid[i+h][j] for h in range(3) if 0<grid[i+h][j]<=9])
        col2 = set([grid[i+h][j+1] for h in range(3) if 0<grid[i+h][j+1]<=9])
        col3 = set([grid[i+h][j+2] for h in range(3) if 0<grid[i+h][j+2]<=9])
        if (sum(col1) != sum(col2) != sum(col3)) or (len(col1) < 3 or len(col2) < 3 or len(col3) < 3):
            return False
        diag1, diag2  = set([grid[i][j], grid[i+1][j+1], grid[i+2][j+2]]), set([grid[i+2][j], grid[i+1][j+1], grid[i][j+2]])
        if (sum(diag1) != sum(diag2)) or (len(diag1) < 3 or len(diag2) < 3):
            return False
        if sum(diag1) != sum(col1) != sum(row1):
            return False
        return True
    
    for i in range(len(grid)-2):
        for j in range(len(grid[0])-2):
            if checkSquare(i, j):
                magic_squares += 1
    
    return magic_squares 

print(numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))