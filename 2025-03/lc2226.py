from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low,high=1,max(candies)+1
        while low<high:
            mid = low + (high-low)//2
            count = 0
            for c in candies:
                count += c//mid
            if count >= k:
                low = mid+1
            else:
                high = mid
        return low-1
s = Solution()
print(s.maximumCandies([9,10,1,2,10,9,9,10,2,2],3))