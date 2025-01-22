from typing import List
from collections import deque

def minPatches(nums: List[int], n: int) -> int:
  patches = 0
  s = 1
  i = 0

  while s <= n:
    if i < len(nums) and nums[i] <= s:
      s += nums[i]
      i += 1
    else:
      s += s
      patches += 1
    
  return patches

print(minPatches([1,2,31,33], 2147483647))