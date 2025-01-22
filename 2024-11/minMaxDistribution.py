from typing import List
from heapq import heappop, heappush
import math


def minimizedMaximum(n: int, quantities: List[int]) -> int:
    l, r = 1, max(quantities)
    while l < r:
        mid = l+(r-l)//2
        if sum([math.ceil(q/mid) for q in quantities]) <= n:
            r = mid
        else:
            l = mid+1
    return l

print(minimizedMaximum(6, [11,6]))
    