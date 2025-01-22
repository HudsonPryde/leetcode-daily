from typing import List
from heapq import heappop, heappush


def maxScoreSightseeingPair(values: List[int]) -> int:
    res = 0
    curr = 0
    for v in values:
        curr -= 1
        if curr + v > res:
            res = curr + v
        if v > curr:
            curr = v
    return res

print(maxScoreSightseeingPair([7,2,6,6,9,4,3]))

