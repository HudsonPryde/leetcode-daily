from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        zeros = 0
        for i in range(n):
            if i < n-1 and nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1] = 0
            if nums[i] != 0:
                res.append(nums[i])
            else:
                zeros += 1
        return res + [0]*zeros
s = Solution()
print(s.applyOperations([1,2,2,1,1,0]))
            