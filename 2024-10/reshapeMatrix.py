from typing import List


def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    if len(mat)*len(mat[0]) != r*c: return mat
    res = [[] for _ in range(r)]
    r_i = 0
    c_i = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            res[r_i].append(mat[i][j])
            c_i += 1
            if c_i >= c:
                r_i += 1
                c_i = 0

    return res

print(matrixReshape([[1,2],[3,4]], 1, 4))