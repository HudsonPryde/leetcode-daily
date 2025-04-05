from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for num in nums:
            res |= num
        return res << (n-1)

s = Solution()
print(s.subsetXORSum([3,4,5,6,7,8]))