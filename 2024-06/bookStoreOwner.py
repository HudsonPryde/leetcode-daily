from typing import List
import functools

def maxSatisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
  min_satisfied = 0
  max_satisfied = 0

  for i in range(minutes):
    max_satisfied += customers[i] if grumpy[i] else 0
    min_satisfied += customers[i] if (not grumpy[i]) else 0

  curr_satisfies = max_satisfied
  for i in range(minutes, len(grumpy)):
    min_satisfied += customers[i] if (not grumpy[i]) else 0
    curr_satisfies += customers[i] if grumpy[i] else 0
    curr_satisfies -= customers[i-minutes] if grumpy[i-minutes] else 0
    max_satisfied = max(max_satisfied, curr_satisfies)
  
  return min_satisfied + max_satisfied

print(maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3))