from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        d = {}
        n = len(nums)
        pairs = 0
        res = 0
        j = 0
        for i in range(n):
            if nums[i] in d:
                pairs += d[nums[i]]
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
            while pairs >= k:
                res += n - i
                d[nums[j]] -= 1
                pairs -= d[nums[j]]
                j += 1
        return res

s = Solution()
print(s.countGood([1,2,2,3,1,1,1],3))