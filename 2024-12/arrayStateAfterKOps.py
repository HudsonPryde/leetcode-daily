from typing import List
from heapq import heappop, heappush

def getFinalState(nums: List[int], k: int, multiplier: int) -> List[int]:
    arr = []
    for i,x in enumerate(nums):
        heappush(arr, (x,i))
    for _ in range(k):
        num,i = heappop(arr)
        nums[i] *= multiplier
        heappush(arr, (num*multiplier,i))

    return nums

print(getFinalState([2,1,3,5,6], 5, 2))