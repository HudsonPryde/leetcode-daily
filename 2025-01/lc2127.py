from typing import List
from collections import defaultdict, deque

def maximumInvitations(favorite: List[int]) -> int:
    n = len(favorite)
    degrees = [0]*n
    depth = [1]*n
    for i in range(n):
        degrees[favorite[i]] += 1
    q = deque([x for x in range(n) if degrees[x] == 0])
    while q:
        node = q.popleft()
        next = favorite[node]
        degrees[next] -= 1
        depth[next] = max(depth[next], depth[node]+1)
        if degrees[next] == 0: q.append(next)
    res = 0
    cycle = 0
    for i in range(n):
        if degrees[i] == 0: continue
        node = i
        l = 0
        while degrees[node] != 0:
            degrees[node] = 0
            node = favorite[node]
            l += 1
        if l == 2:
            cycle += depth[i] + depth[favorite[i]]
        else:
            res = max(l, res)
    return max(cycle, res)

print(maximumInvitations([1, 0, 0, 2, 1, 4, 7, 8, 9, 6, 7, 10, 8]))
