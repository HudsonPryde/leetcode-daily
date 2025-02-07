from typing import List


def queryResults(limit: int, queries: List[List[int]]) -> List[int]:
    res = []
    count = {}
    coloured = {}
    for x,y in queries:
        if x in coloured:
            c = coloured[x]
            count[c] -= 1
            if count[c] == 0:
                del count[c]
        coloured[x] = y
        count[y] = count.get(y, 0)+1
        res.append(len(count.keys()))
    return res

print(queryResults(4, [[0,1],[1,2],[2,2],[3,4],[4,5]]))
