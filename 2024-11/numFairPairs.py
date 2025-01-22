from typing import List


def countFairPairs(nums: List[int], lower: int, upper: int) -> int:
    nums.sort()
    return helper(upper + 1, nums) - helper(lower, nums)
def helper(k: int, nums: List[int]) -> int:
        l, h = 0, len(nums)-1
        res = 0
        while l < h:
            s = nums[l] + nums[h]
            if s < k:
                res += h-l
                l += 1
            else:
                h -= 1
        return res
print(countFairPairs([1,7,5,9,2,11],12,12))
