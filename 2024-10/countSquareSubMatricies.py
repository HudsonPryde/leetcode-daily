from typing import List


def countSquares(matrix: List[List[int]]) -> int:
    r,c = len(matrix), len(matrix[0])
    # smaller of r and c is max matrix dim
    d = min(r,c)
    count = 0

    def _check_valid(d: int, i: int, j: int):
        # check for zeros in the submatrix
        for h in range(d):
            for g in range(d):
                if matrix[j+h][i+g] == 0:
                    return False
        return True
    
    # check each submatrix of size d to 2
    for k in range(1, d+1):
        # move the sub matrix along the diff between its h and w and the original matrix
        # start at row 0
        # move along the cols
        for j in range(r-k+1):
            for i in range(c-k+1):
                # check the submatrix of k, i, j dims
                if _check_valid(k, i, j):
                    count += 1
    return count
    
print(countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))