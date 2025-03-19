from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n-2):
            if nums[i] == 0:
                res += 1
                nums[i],nums[i+1],nums[i+2] = 1, int(not nums[i+1]), int(not nums[i+2])
        return res if not 0 in nums[-3:] else -1

s = Solution()
print(s.minOperations([0,0,1,0,0,1,0]))