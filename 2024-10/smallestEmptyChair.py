from typing import List
from heapq import heappush, heappop


def smallestChair(times: List[List[int]], targetFriend: int) -> int:
    n = len(times)
    target = times[targetFriend]
    occupied = []
    unoccupied = [i for i in range(n)]
    t = 0
    times.sort()
    for i in range(n):
        a,d = times[i]
        t = a
        while occupied and occupied[0][0] <= t:
            _,c = heappop(occupied)
            heappush(unoccupied, c)
        if t == target[0]:
            return heappop(unoccupied)
        heappush(occupied, (d,heappop(unoccupied)))
    return n

print(smallestChair([[1,2],[2,3]], 1))

