from typing import List
from collections import deque

def maximumSubarraySum(nums: List[int], k: int) -> int:
    n = len(nums)
    max_sum = 0
    curr_sum = 0
    window = deque()
    content = set()
    for i in range(n):
        while nums[i] in content:
            p = window.popleft()
            content.remove(p)
            curr_sum -= p
        window.append(nums[i])
        content.add(nums[i])
        curr_sum += nums[i]
        if len(window) > k:
            p = window.popleft()
            content.remove(p)
            curr_sum -= p
        if len(window) == k:
            max_sum = max(curr_sum, max_sum)

    return max_sum



print(maximumSubarraySum([1,5,4,2,9,9,9], 3))