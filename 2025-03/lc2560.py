from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n= len(nums)
        min_nums = sorted(nums)
        def check(cap:int):
            c = 0
            i = 0
            while i < n:
                if nums[i] <= cap:
                    i += 2
                    c += 1
                else:
                    i += 1
                if c == k:
                    return True
            return False
        low,high = 0,n-1
        while low<high:
            mid = low + (high-low)//2
            if check(min_nums[mid]):
                high = mid
            else:
                low = mid+1
        return min_nums[low]

s = Solution()
print(s.minCapability([4,22,11,14,25],3))