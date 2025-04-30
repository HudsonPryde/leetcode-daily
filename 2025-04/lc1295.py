from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([x for x in [str(xs) for xs in nums] if len(x)%2==0])
s = Solution()
print(s.findNumbers([12,345,2,6,7896]))