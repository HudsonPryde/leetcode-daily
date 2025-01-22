from typing import List


def maxDistance(arrays: List[List[int]]) -> int:
    max_d, min_d = arrays[0][-1], arrays[0][0]
    res = float('-inf')
    for i in range(1, len(arrays)):
        l,k = abs(max_d-arrays[i][0]), abs(arrays[i][-1]-min_d)
        if l > k:
            if l > res:
                res = l
        else:
            if k > res:
                res = k
        min_d = min(min_d, arrays[i][0], arrays[i][-1])
        max_d = max(max_d, arrays[i][0], arrays[i][-1])
    return res

print(maxDistance([[1,3],[-10,-9,2,2,3,4],[-8,-5,2],[-10,-6,-5,-5,0,3],[-8,-6,-2,0,2,3,3],[-10,-10,-5,0]]))