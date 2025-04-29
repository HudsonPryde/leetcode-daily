from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums)
        n = len(nums)
        pos = []
        res = 0
        for i in range(n):
            num = nums[i]
            if num == m:
                pos.append(i)
            if len(pos) >= k:
                res += pos[-k]+1
        return res

s = Solution()
print(s.countSubarrays([28,5,58,91,24,91,53,9,48,85,16,70,91,91,47,91,61,4,54,61,49],1))
                
            


