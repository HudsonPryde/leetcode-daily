from typing import List
import math


def minimumSize(nums: List[int], maxOperations: int) -> int:
    l,h = 1, max(nums)
    def helper(mid:int,nums,maxOp):
        totalOp = 0
        for num in nums:
            ops = math.ceil(num/mid)-1
            totalOp += ops
            if totalOp > maxOp:
                return False
        return True
    while l < h:
        mid = l+(h-l)//2
        if helper(mid, nums, maxOperations):
            h = mid
        else:
            l = mid+1
    return l
print(minimumSize([9],2))