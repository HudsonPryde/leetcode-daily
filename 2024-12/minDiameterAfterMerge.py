from typing import List
from collections import defaultdict, deque


def minimumDiameterAfterMerge(edges1: List[List[int]], edges2: List[List[int]]) -> int:
    n1,n2 = len(edges1),len(edges2)
    adj1 = defaultdict(list)
    adj2 = defaultdict(list)
    
    degrees1, degrees2 = defaultdict(int),defaultdict(int)
    for i in range(max(n1,n2)):
        if i < n1:
            a,b = edges1[i]
            adj1[a].append(b)
            adj1[b].append(a)
            degrees1[a] += 1
            degrees1[b] += 1
        if i < n2:
            a,b = edges2[i]
            adj2[a].append(b)
            adj2[b].append(a)
            degrees2[a] += 1
            degrees2[b] += 1
    q1 = deque([k for k,v in degrees1.items() if v == 1])
    q2 = deque([k for k,v in degrees2.items() if v == 1])
    root1 = 0
    root2 = 0
    values1 = defaultdict(int)
    values2 = defaultdict(int)
    d1,d2 = 0,0
    while q1:
        curr = q1.popleft()
        v = values1[curr] + 1
        degrees1[curr] -= 1
        for x in adj1[curr]:
            if degrees1[x] == 0: continue
            d1 = max(d1, values1[x]+v)
            values1[x] = max(values1[x], v)
            degrees1[x] -= 1
            if degrees1[x] == 1:
                q1.append(x)
        if not q1:
            root1 = curr
    while q2:
        curr = q2.popleft()
        v = values2[curr] + 1
        degrees2[curr] -= 1
        for x in adj2[curr]:
            if degrees2[x] == 0: continue
            d2 = max(d2, values2[x]+v)
            values2[x] = max(values2[x], v)
            degrees2[x] -= 1
            if degrees2[x] == 1:
                q2.append(x)
        if not q2:
            root2 = curr
    
    return max(values1[root1]+values2[root2]+1,d1,d2)
print(minimumDiameterAfterMerge([[0,1],[2,0],[3,2],[3,6],[8,7],[4,8],[5,4],[3,5],[3,9]], [[0,1],[0,2],[0,3]]))