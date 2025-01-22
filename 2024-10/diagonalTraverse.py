from typing import List


def findDiagonalOrder(mat: List[List[int]]) -> List[int]:
    r, c = len(mat), len(mat[0])
    n = r+c-1

    res = []
    d = 0
    for i in range(r):
        m = []
        for j in range(i+1):
            if j>=c or i-j>=r: break 
            m.append(mat[i-j][j])
        if d%2 != 0:
            res.append(m[::-1])
        else:
            res.append(m)
        d += 1
    
    for i in range(1, c):
        m = []
        for j in range(c-i):
            if r-1-j < 0 or i+j > c: break
            m.append(mat[r-1-j][i+j])
        if d%2 != 0:
            res.append(m[::-1])
        else:
            res.append(m)
        d += 1
        
    return res

print(findDiagonalOrder([[6,9,7]]))
