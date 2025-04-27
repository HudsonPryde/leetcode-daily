from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n-2):
            if nums[i+1]/2 == nums[i]+nums[i+2]:
                res += 1
        return res