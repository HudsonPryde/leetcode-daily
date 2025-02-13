from heapq import heapify, heappop, heappush
from typing import List


def minOperations(nums: List[int], k: int) -> int:
    heapify(nums)
    res = 0
    while nums[0] < k:
        a,b = heappop(nums), heappop(nums)
        heappush(nums, min(a,b)*2+max(a,b))
        res += 1
    return res

print(minOperations([2,11,10,1,3], 10))