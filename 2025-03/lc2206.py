from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            d[num] = 0 if d.get(num,0) == 1 else 1
        return True if sum(d.values()) == 0 else False

s = Solution()
print(s.divideArray([1,2,3,4]))

