from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [-1]*(n+1)
        res = []
        for i in range(n):
            res = max(res,self._helper(i,nums,dp),key=lambda x: len(x))
        return res
    def _helper(self,i:int,nums:list,dp:list):
        if dp[i] != -1:
            return dp[i]
        seq = []
        for j in range(i+1,len(nums)):
            if nums[j] % nums[i] == 0:
                seq = max(seq,self._helper(j,nums,dp),key=lambda x: len(x))
        dp[i] = [nums[i]] + seq
        return dp[i]

s = Solution()
print(s.largestDivisibleSubset([5,9,18,54,108,540,90,180,360,720]))