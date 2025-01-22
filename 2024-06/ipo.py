from typing import List
from heapq import heappush, heappop, nlargest

def findMaximizedCapital(k: int, w: int, profits: List[int], capital: List[int]) -> int:
  if w >= max(capital):
    return w + sum(nlargest(k, profits))
  
  d = list(zip(profits, capital))
  d.sort(key=lambda x: x[1])
  o = []

  for _ in range(k):
    while d and d[0][1] <= w:
      heappush(o, -1*d.pop(0)[0])
    if not o:
      break
    w += -heappop(o)
  return w

print(findMaximizedCapital(3, 0, [1,2,3], [0,1,2]))