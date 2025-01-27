from typing import List
from collections import defaultdict, deque


def checkIfPrerequisite(n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    d = defaultdict(list)
    for a,b in prerequisites:
        d[b].append(a)
    res = []
    reqs = [set() for _ in range(n)]

    def helper(node):
        for u in d[node]:
            if u not in reqs[node]:
                reqs[node].add(u)
                reqs[node].update(helper(u))
        return reqs[node]
    for i in range(n):
        helper(i)
    for u,v in queries:
        res.append(u in reqs[v])
    return res

print(checkIfPrerequisite(4, [[2,3],[2,1],[0,3],[0,1]], [[0,1],[0,3],[2,3],[3,0],[2,0],[0,2]]))