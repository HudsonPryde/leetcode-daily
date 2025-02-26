from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        minSum = float('inf')
        currMaxSum = 0
        currMinSum = 0
        n = len(nums)
        for i in range(n):
            if currMaxSum >= 0:
                currMaxSum += nums[i]
            else:
                currMaxSum = nums[i]
            maxSum = max(currMaxSum,maxSum)
            if currMinSum >= 0:
                currMinSum = nums[i]
            else:
                currMinSum += nums[i]
            minSum = min(currMinSum,minSum)
        return max(maxSum,abs(minSum))
    
s = Solution()
print(s.maxAbsoluteSum([1,-3,2,3,-4]))