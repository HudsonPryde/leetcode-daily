from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        l,t,j = 0,0,0
        for i in range(n):
            l += 1
            t += nums[i]
            if t*l < k:
                res += l
            else:
                for h in range(j,i+1):
                    t -= nums[h]
                    l -= 1
                    if t*l < k:
                        j = h+1
                        res += l
                        break
        return res

s = Solution()
print(s.countSubarrays([2,1,4,3,5],10))