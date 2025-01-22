from typing import List

def heightChecker(heights: List[int]) -> int:
  o = 0
  e = sorted(heights)
  for i in range(len(heights)):
    if heights[i] != e[i]:
      o += 1
  return o

print(heightChecker([1,1,4,2,1,3]))