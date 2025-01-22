from typing import List

def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
  arr1.sort()
  d = {}
  for n in arr1:
    d[n] = d.get(n, 0)+1
  o = []
  for r in arr2:
    o.append([r]*d[r])
    del d[r]
  
  for k,v in d.items():
    o.append([k]*v)
  return [x for xs in o for x in xs]

print(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))