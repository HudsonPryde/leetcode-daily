from typing import List


def maxWidthRamp(nums: List[int]) -> int:
    n = len(nums)
    ind = []
    max_w = 0
    for i in range(n):
        if not ind or nums[ind[-1]] > nums[i]:
            ind.append(i)
    
    for j in range(n-1,-1,-1):
        while ind and nums[ind[-1]] <= nums[j]:
            max_w = max(max_w, j-ind[-1])
            ind.pop()

    return max_w

print(maxWidthRamp([6,0,8,2,1,5]))