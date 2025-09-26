from typing import List
from bisect import bisect_right,bisect_left
from math import factorial
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == 0: continue
            for j in range(i+1,len(nums)):
                p = bisect_left(nums, nums[i]+nums[j], j)
                count += p-j-1
        return count



print(Solution().triangleNumber([16,24,29,6,48,24,44,27,7,6,17,51,37,19,23,0,20,42,49,41,46]))