from typing import List


def firstCompleteIndex(arr: List[int], mat: List[List[int]]) -> int:
    n,m = len(mat), len(mat[0])
    rows = [0]*n
    cols = [0]*m
    d = [0]*(n*m+1)
    for r in range(n):
        for c in range(m):
            d[mat[r][c]] = (r,c)
    for i in range(len(arr)):
        r,c = d[arr[i]]
        rows[r] += 1
        cols[c] += 1
        if rows[r] == m or cols[c] == n:
            return i
    return len(arr)-1

print(firstCompleteIndex([6,2,3,1,4,5], [[5,1],[2,4],[6,3]]))