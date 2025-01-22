from typing import List

def minIncrementForUnique(nums: List[int]) -> int:
  freq = [0] * (len(nums) + max(nums) + 1)
  o = 0

  for n in nums:
    freq[n] += 1
  
  for i in range(len(freq)):
    if freq[i] > 1:
      e = freq[i] - 1
      freq[i + 1] += e
      o += e
  return o
print(minIncrementForUnique([2,2,2,2,0]))