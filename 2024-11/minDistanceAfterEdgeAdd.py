from typing import List


def shortestDistanceAfterQueries(n: int, queries: List[List[int]]) -> List[int]:
    d = {}
    for i in range(n):
        if i < n-1:
            d[i] = [i+1]
        else:
            d[i] = None

    res = []
    min_steps = [n-i-1 for i in range(n)]
    for u,v in queries:
        start, end = min(u,v), max(u,v)
        d[start].append(end)
        # if this edge is a better path than what is available currently
        # update min steps
        if min_steps[end]+1 < min_steps[start]:
            min_steps[start] = min_steps[end]+1
        else:
            # if its not better add the curr best abth from start and continue
            res.append(min_steps[0])
            continue
        # go backwards from the starting point of the new edge updating the best paths
        for i in range(start, -1, -1):
            # no edges means the end
            if not d[i]: continue
            # for each edge of node the possible paths are the curr min steps of the nodes it connects to + 1
            can = [min_steps[x]+1 for x in d[i]]
            # best path is the curr min of its edges
            min_steps[i] = min(can)
        # add best option from start
        res.append(min_steps[0])
    return res

print(shortestDistanceAfterQueries(14, [[0,6],[4,12]]))
