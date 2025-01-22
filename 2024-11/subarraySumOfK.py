from typing import List
from collections import deque

def shortestSubarray(nums: List[int], k: int) -> int:
    n = len(nums)
    p_sums = [0]*(n+1)

    # find prefixes
    for i in range(1, n+1):
        p_sums[i] = p_sums[i-1]+nums[i-1]
    
    indicies = deque()
    min_len = float('inf')

    for i in range(n+1):
        # remove index from front while sum >= k
        while indicies and p_sums[i] - p_sums[indicies[0]] >= k:
            min_len = min(min_len, i-indicies.popleft())
        
        # maintain mono queue
        while indicies and p_sums[i] <= p_sums[indicies[-1]]:
            indicies.pop()
        
        indicies.append(i)
    
    return min_len if min_len != float('inf') else -1


print(shortestSubarray([-28,81,-20,28,-29],89))