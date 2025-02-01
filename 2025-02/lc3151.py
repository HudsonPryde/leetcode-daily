from typing import List


def isArraySpecial(nums: List[int]) -> bool:
    n = len(nums)
    for i in range(1, n):
        if nums[i]%2 == nums[i-1]%2:
            return False
    return True

print(isArraySpecial([4,3,1,6]))