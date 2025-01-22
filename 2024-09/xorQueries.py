from typing import List


def xorQueries(arr: List[int], queries: List[List[int]]) -> List[int]:
    res = []
    n = len(arr)
    m = [0]*n
    m[0] = arr[0]
    for i in range(1, n):
        m[i]=(m[i-1]^arr[i])
    print(m)
    for start,stop in queries:
        if start == 0:
            res.append(m[stop])
        else:
            res.append(m[stop]^m[start-1])
    return res
print(xorQueries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]))