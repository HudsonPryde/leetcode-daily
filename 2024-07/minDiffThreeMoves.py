
from typing import List


def minDifference(nums: List[int]) -> int:
  if len(nums) <= 4:
    return 0
  nums.sort()
  min_diff = float('inf')
  for i in range(4):
    min_val, max_val = nums[i], nums[len(nums)-4+i]
    min_diff = min(min_diff, (max_val - min_val))
  return min_diff

  

print(minDifference([5,3,2,4]), "expect: 0")
print(minDifference([3,100,20]), "expect: 0")
print(minDifference([1,5,0,10,14]), "expect: 1")
print(minDifference([6,6,0,1,1,4,6]), "expect: 2")
print(minDifference([82,81,95,75,20]), "expect: 1")
  