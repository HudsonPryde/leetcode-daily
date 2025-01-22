from typing import List


def findRotation(mat: List[List[int]], target: List[List[int]]) -> bool:
    n = len(mat)
    for _ in range(4):
        for i in range(n):
            for j in range(i):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        for i in range(n):
            mat[i] = mat[i][::-1]
        if mat == target: return True