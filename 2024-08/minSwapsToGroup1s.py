from collections import Counter
from typing import List


def minSwaps(nums: List[int]) -> int:
    ones = sum(nums)
    n = len(nums)
    
    window = sum(nums[:ones])
    min_swaps = ones - window

    for i in range(n):
        window += nums[i % n]
        window -= nums[i - ones]
        min_swaps = min(min_swaps, ones-window)

    return min_swaps
# print(minSwaps([1,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,1,0,1,1,0,1,1,0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,1,1,1,0,0,0,1,0,1,1,1,1,0,0,0,1,1,0,1,1,0,0,0,1,1,1,0,1,1,0,1,0,0,1,0,0,1,1,1,0,1,1,0,0,0,1,1,0,1,1,0,1,0,1,1,0,0,1,1,1,0,1,0,0,1,1,0,0,1,1,0,0,0]))
print(minSwaps([0,1,0,1,1,0,0]))