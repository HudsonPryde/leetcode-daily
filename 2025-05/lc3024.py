from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0]+nums[1] <= nums[2]: return 'none'
        if nums[1]+nums[2] <= nums[0]: return 'none'
        if nums[2]+nums[0] <= nums[1]: return 'none'
        types = ['equilateral', 'isosceles', 'scalene']
        return types[len(set(nums))-1]