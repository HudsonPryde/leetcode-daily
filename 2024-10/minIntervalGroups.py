from typing import List
from heapq import heappush, heapreplace


def minGroups(intervals: List[List[int]]) -> int:
    intervals.sort()
    heap = []
    for start, end in intervals:
        if not heap:
            heappush(heap, end)
            continue
        if start > heap[0]:
            heapreplace(heap, end)
        else:
            heappush(heap,end)
    return len(heap)

print(minGroups([[1,3],[5,6],[8,10],[11,13]]))