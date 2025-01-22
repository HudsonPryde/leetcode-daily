from typing import List
from heapq import heappop, heappush


def continuousSubarrays(nums: List[int]) -> int:
    n = len(nums)
    slow = 0
    res = 0
    h = []
    d = {}
    for i in range(n):
        d[nums[i]] = d.get(nums[i], 0) + 1
        if d[nums[i]] == 1:
                heappush(h, nums[i]*-1)
        if not (0 <= abs((h[0]*-1) - nums[i]) <= 2):
            res += ((i-slow)*(i-slow+1)//2) - (i-slow)
        while not (0 <= abs((h[0]*-1) - nums[i]) <= 2):
            d[nums[slow]] -= 1
            if h[0]*-1 == nums[slow] and d[nums[slow]] == 0:
                heappop(h)
            slow += 1
    res += ((i-slow+1)*(i-slow+2)//2) - (i-slow+1)
    return res+n
print(continuousSubarrays([1,2,3]))