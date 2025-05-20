from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        d = [0]*(n+1)
        d[0] = nums[0]
        for i in range(1,n):
            d[i] = nums[i] - nums[i-1]
        
        for l,r in queries:
            d[l] += -1
            d[r+1] -= -1
        
        for i in range(n):
            if i == 0:
                nums[i] = d[i]
            else:
                nums[i] = d[i] + nums[i-1]
            if nums[i] > 0:
                return False
        return True

s = Solution()
print(s.isZeroArray([1,0,1], [[0,2]]))