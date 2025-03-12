from typing import List
from bisect import bisect_left,bisect_right

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = bisect_left(nums,0),bisect_right(nums,0)
        numNeg = n-(n-r)-(r-l)
        numPos = n-numNeg-(r-l)
        return numNeg,numPos
s = Solution()
print(s.maximumCount([-3,-2,-1,0,0,1,2]))
