from typing import List


def isToeplitzMatrix(matrix: List[List[int]]) -> bool:
    r, c = len(matrix), len(matrix[0])

    for i in range(r):
        prev = matrix[i][0]
        for j in range(c):
            if i+j >= r: break
            if prev != matrix[i+j][j]:
                return False
    for i in range(1, c):
        prev = matrix[0][i]
        for j in range(r):
            if i+j >= c: break
            if prev != matrix[j][i+j]:
                return False
    return True


    

print(isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
#[[22,0,94,45,46,96],
# [10,22,80,94,45,46]]