from typing import List

def minDays(bloomDay: List[int], m: int, k: int) -> int:
  if len(bloomDay) < m*k:
    return -1
  low = 1
  high = max(bloomDay)

  while low < high:
    mid = (low + high) // 2
    if validBouquets(bloomDay, mid, m, k):
      high = mid
    else:
      low = mid+1
  return low


def validBouquets(bloomDay, d, m, k):
  f = 0
  t = 0
  for b in bloomDay:
      if b <= d:
          f += 1
          if f == k:
              t += 1
              f = 0
      else:
          f = 0
  return t >= m


  
print(minDays([1,10,3,10,2], 3, 1))