from typing import List


def findChampion(n: int, edges: List[List[int]]) -> int:
    candidates = set([i for i in range(n)])
    for u,v in edges:
        if v in candidates:
            candidates.remove(v)
    if len(candidates) > 1: return -1
    else: return list(candidates)[0]

print(findChampion(4, [[0,2],[1,3],[1,2]]))