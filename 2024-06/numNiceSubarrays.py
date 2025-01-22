from typing import List

def numberOfSubarrays(nums: List[int], k: int) -> int:
  sums = {0: 1}
  curr_sum = 0
  total = 0

  for num in nums:
    curr_sum += num % 2
    if (curr_sum - k) in sums:
      total += sums[curr_sum - k]
    sums[curr_sum] = sums.get(curr_sum, 0) + 1
  return total


print(numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2))