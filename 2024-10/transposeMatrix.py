from typing import List


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    r,c = len(matrix), len(matrix[0])
    res = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            res[j][i] = matrix[i][j]
    return res