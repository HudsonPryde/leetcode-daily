from typing import List


def construct2DArray(original: List[int], m: int, n: int) -> List[List[int]]:
    if n*m != len(original):
        return []
    res = []
    for i in range(m):
        res.append(original[i*n : (i*n)+n])
    return res
print(construct2DArray([1,2,3],1,3))
