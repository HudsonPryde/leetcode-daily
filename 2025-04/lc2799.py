from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        k = len(set(nums))
        cur = set()
        j = 0
        res = 0
        for i in range(n):
            num = nums[i]
            d[num] = d.get(num,0)+1
            if num not in cur:
                cur.add(num)
            while d[nums[j]] > 1:
                d[nums[j]] -= 1
                j += 1
            if len(cur) == k:
                res += 1+j
        return res
s = Solution()
print(s.countCompleteSubarrays([1898,370,822,1659,1360,128,370,360,261,1898]))
