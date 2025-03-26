from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = sorted([x for xs in grid for x in xs])
        return self._check_valid(nums,nums[len(nums)//2],x)
    def _check_valid(self,nums:List[int],target:int,x:int):
        res = 0
        for num in nums:
            k = abs(target-num)
            if k%x != 0:
                return -1
            res += k//x
        return res

s = Solution()
print(s.minOperations([[1,2],[3,4]],2))