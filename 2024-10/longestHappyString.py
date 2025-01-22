from heapq import heapify, heappop, heappush


def longestDiverseString(a: int, b: int, c: int) -> str:
    m = ['a','b','c']
    c = [a,b,c]
    heap = [(-c[i], m[i]) for i in range(3) if c[i] > 0]
    heapify(heap)
    res = ''
    prev = ''

    while heap:
        d = heappop(heap)
        if d[1] == prev:
            if not heap:
                break
            g = heappop(heap)
            if g[0] < d[0]//2:
                v = min(g[0]*-1, 2)
            else:
                v = 1
            res += g[1]*v
            if g[0] + v < 0:
                heappush(heap, (g[0]+v, g[1]))
        if d[0] < 0:
            v = min(d[0]*-1, 2)
            res += d[1]*v
            if d[0] + v < 0:
                heappush(heap, (d[0]+v, d[1]))
            prev = d[1]
    return res
        
            
print(longestDiverseString(3,40,7))