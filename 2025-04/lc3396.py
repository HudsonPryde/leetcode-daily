from typing import List
import math

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        idx = -1
        n = len(nums)
        # find the last index of a duplicated num
        d = set()
        for i in range(n-1,-1,-1):
            if nums[i] in d:
                idx = i
                break
            else:
                d.add(nums[i])
        if idx == -1: return 0
        return math.ceil((idx+1)/3)

s = Solution()
print(s.minimumOperations([10, 10, 10, 10, 10]))