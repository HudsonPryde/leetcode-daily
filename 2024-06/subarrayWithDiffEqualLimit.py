from typing import List
from collections import deque

def longestSubarray(nums: List[int], limit: int) -> int:
  longest_len = 0
  current_len = 0

  max_q, min_q = deque(), deque()

  for i in range(len(nums)):
    while min_q and nums[min_q[-1]] > nums[i]:
      min_q.pop()
    min_q.append(i)

    while max_q and nums[max_q[-1]] < nums[i]:
      max_q.pop()
    max_q.append(i)

    current_len += 1

    while current_len >= 1 and nums[max_q[0]] - nums[min_q[0]] > limit:
      if min_q and min_q[0] == i - current_len + 1:
        min_q.popleft()
      if max_q and max_q[0] == i - current_len + 1:
        max_q.popleft()
      
      current_len -= 1
    
    if current_len >= 1 and longest_len < current_len:
      longest_len = current_len
    

  return longest_len

print(longestSubarray([8,2,4,7], 4), " expect: 2")
print(longestSubarray([10,1,2,4,7,2], 5), " expect: 4")
print(longestSubarray([4,2,2,2,4,4,2,2], 0), " expect: 3")
print(longestSubarray([1, 1000000000, 1, 1000000000], 1000000000), " expect: 4")
print(longestSubarray([24,12,71,33,5,87,10,11,3,58,2,97,97,36,32,35,15,80,24,45,38,9,22,21,33,68,22,85,35,83,92,38,59,90,42,64,61,15,4,40,50,44,54,25,34,14,33,94,66,27,78,56,3,29,3,51,19,5,93,21,58,91,65,87,55,70,29,81,89,67,58,29,68,84,4,51,87,74,42,85,81,55,8,95,39], 87), " expect: 25")
print(longestSubarray([7,40,10,10,40,39,96,21,54,73,33,17,2,72,5,76,28,73,59,22,100,91,80,66,5,49,26,45,13,27,74,87,56,76,25,64,14,86,50,38,65,64,3,42,79,52,37,3,21,26,42,73,18,44,55,28,35,87], 63), " expect: 9")