from typing import List
from collections import defaultdict, deque


def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  # Write your code here
    order = deque([])
    prev = defaultdict(int)
    res = 0
    for d in D:
        if not prev.get(d, 0):
            res += 1
            order.append(d)
            prev[d] += 1
        if len(order) > K:
            o = order.popleft()
            prev[o] -= 1
    return res

print(getMaximumEatenDishCount(6, [1,2,3,3,2,1], 2))