from typing import List


def maxAscendingSum(nums: List[int]) -> int:
    n = len(nums)
    res = nums[0]
    curr = res
    for i in range(1,n):
        if nums[i] <= nums[i-1]:
            res = max(res,curr)
            curr = nums[i]
        else:
            curr += nums[i]
            res = max(res,curr)
    return res

print(maxAscendingSum([10,20,30,5,10,50]))