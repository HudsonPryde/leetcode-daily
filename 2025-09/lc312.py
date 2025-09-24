from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # balloon selected nets its points + surrounding 2 balloons points
        # after selected it is removed from array
        # dp algo trying every option while keeping track of best option for array state
        dp = {}
        return self.helper(nums, dp)
    def helper(self, nums: List[int], dp: dict):
        t_nums = tuple(nums)
        if t_nums in dp: return dp[t_nums]
        # recurse for every balloon in the array
        # return the max coins you can get
        max_coins = 0
        for i in range(len(nums)):
            coins = nums[i]
            coins *= 1 if 0>i-1 else nums[i-1]
            coins *= 1 if i+1>=len(nums) else nums[i+1]
            new_l = nums[:i]+nums[i+1:]
            max_coins = max(max_coins, coins + self.helper(new_l,dp))
        dp[t_nums] = max_coins
        return dp[t_nums]

print(Solution().maxCoins([3,1,5,8]))