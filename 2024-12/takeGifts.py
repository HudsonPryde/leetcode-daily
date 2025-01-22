from typing import List
from heapq import heappop, heappush, heapify
import math

def pickGifts(gifts: List[int], k: int) -> int:
    gifts = [g*-1 for g in gifts]
    heapify(gifts)
    for i in range(k):
        g = heappop(gifts)*-1
        g = math.floor(math.sqrt(g))
        heappush(gifts, g*-1)
    return -1*sum(gifts)
print(pickGifts([25,64,9,4,100], 4))
