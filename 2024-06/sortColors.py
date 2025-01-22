from typing import List
def sortColors(nums: List[int]) -> None:
  i = 0
  e = 1
  for y in range(len(nums)):
    if nums[i] == 0:
      i+=1
      continue
    if nums[i] == 1:
      if len(nums)-e == i:
        break
      nums.insert(len(nums)-e, nums.pop(i))
      continue
    if nums[i] == 2:
      nums.append(nums.pop(i))
      e += 1
      continue
  return nums
print(sortColors([2,0,1]))