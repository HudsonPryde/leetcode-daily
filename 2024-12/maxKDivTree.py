from typing import List
from collections import defaultdict, deque


def maxKDivisibleComponents(n: int, edges: List[List[int]], values: List[int], k: int) -> int:
    if n < 2: return 1
    res = 0
    adj = defaultdict(list)
    degrees = [0]*n
    for a,b in edges:
        adj[a].append(b)
        adj[b].append(a)
        degrees[a] += 1
        degrees[b] += 1
    q = deque([i for i in range(n) if degrees[i] == 1])
    while q:
        curr = q.popleft()
        degrees[curr] -= 1
        addval = 0
        if values[curr]%k == 0:
            res += 1
        else:
            addval = values[curr]
        for x in adj[curr]:
            if degrees[x] == 0: continue
            degrees[x] -= 1
            values[x] += addval
            if degrees[x] == 1:
                q.append(x)
    return res

    

        


    

print(maxKDivisibleComponents(5, [[0,2],[1,2],[1,3],[2,4]], [1,8,1,4,4], 6))