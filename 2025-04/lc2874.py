from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = 0
        max_diff = float('-inf')
        max_trip = 0
        for i in range(n):
            num = nums[i]
            max_trip = max(max_trip,max_diff*num)
            max_diff = max(max_diff,max_val-num)
            max_val = max(max_val,num)
        return max_trip