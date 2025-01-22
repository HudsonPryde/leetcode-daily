from typing import List

def maxDistance(position: List[int], m: int) -> int:
  def checkDistance(value): 
    count = 0
    current_pos = position[0]
    for pos in position:
      if abs(current_pos-pos) >= value:
        current_pos = pos
        count += 1
        if count >= m-1:
          return False
    return True


  position.sort()
  left, right = 0, abs(position[0] - position[-1])+1
  while left < right:
    mid = left + (right - left) // 2
    if checkDistance(mid):
      right = mid
    else:
      left = mid + 1
  return left - 1

print(maxDistance([79,74,57,22], 4))