from typing import List


def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    n = len(edges)
    s = [i for i in range(n+1)]
    res = []

    def helper(node):
        if s[node] == node:
            return node
        return helper(s[node])

    for u,v in edges:
        r1,r2 = helper(u),helper(v)
        if r1 == r2:
            res.append((u,v))
        else:
            if s[v] == v:
                s[v] = r1
            elif s[u] == u:
                s[u] = r2
            else:
                s[r1] = v
    return res[-1]

print(findRedundantConnection([[15,24],[2,8],[19,21],[2,15],[16,25],[7,9],[3,24],[10,20],[13,20],[5,21],[7,11],[6,23],[7,16],[1,8],[17,20],[4,19],[11,22],[5,11],[1,16],[14,20],[1,4],[22,23],[12,20],[15,18],[12,16]]))
