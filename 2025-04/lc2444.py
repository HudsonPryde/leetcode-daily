from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        d = {minK:0,maxK:0}
        n = len(nums)
        j = 0
        k = 0
        res = 0
        for i in range(n):
            num = nums[i]
            
            if num == minK or num == maxK:
                d[num] += 1
            if num > maxK or num < minK:
                d = {minK:0,maxK:0}
                j = i+1
                k = i+1
            else:
                while j < n and (nums[j] not in d or d[nums[j]] > 1):
                    if nums[j] in d: d[nums[j]] -= 1
                    j += 1
                    
            if d[minK] > 0 and d[maxK] > 0:
                res += 1+j-k
        return res
s = Solution()

print(s.countSubarrays([4,3],3,3))