from typing import List


def findThePrefixCommonArray(A: List[int], B: List[int]) -> List[int]:
    n = len(A)
    common = [0]*n
    c = []
    for i in range(n):
        common[i] = common[i-1]
        common[A[i]]+=1
        common[B[i]]+=1
        if common[A[i]] > 1:
            common[i] += 1
        if common[B[i]] > 1:
            common[i] += 1
    return c