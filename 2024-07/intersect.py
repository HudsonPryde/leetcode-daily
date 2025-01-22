from collections import Counter
from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
  c = Counter(nums1)
  output = []
  for num in nums2:
    if num in c:
      if c[num] > 0:
        output.append(num)
        c[num]-=1
  return output



print(intersect([4,9,5], [9,4,9,8,4]))