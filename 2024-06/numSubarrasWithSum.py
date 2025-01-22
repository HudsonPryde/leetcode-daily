from typing import List

def numSubarraywithSum(nums: List[int], goal: int) -> int:
  sums = {0: 1}
  curr_sum = 0
  total = 0

  for num in nums:
    curr_sum += num
    if (curr_sum - goal) in sums:
      total += sums[curr_sum - goal]
    sums[curr_sum] = sums.get(curr_sum, 0) + 1
  return total


print(numSubarraywithSum([1,0,1,0,1,0], 2))