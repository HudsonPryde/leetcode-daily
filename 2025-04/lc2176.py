from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        nums = sorted(enumerate(nums),key=lambda x: x[1])
        n = len(nums)
        res = 0
        for i in range(n):
            idx,num = nums[i]
            for j in range(i+1,n):
                idx2,num2 = nums[j]
                if num2 != num: break
                if (idx*idx2)%k != 0: continue
                res += 1
        return res

