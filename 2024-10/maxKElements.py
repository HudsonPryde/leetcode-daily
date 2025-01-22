from heapq import heapify, heappush, heapreplace
from math import floor
from typing import List


def maxKelements(nums: List[int], k: int) -> int:
    heap = [-num for num in nums]
    heapify(heap)
    res = 0
    for _ in range(k):
        res -= heapreplace(heap, floor(heap[0]/3))
    return res

print(maxKelements([1,10,3,3,3], 3))