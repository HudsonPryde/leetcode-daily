from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 0
        l = 0
        cur = 0
        j = 0
        for i,num in enumerate(nums):
            if cur & num == 0:
                cur += num
                l += 1
                res = max(l,res)
            else:
                while j < i:
                    cur -= nums[j]
                    l -= 1
                    j+= 1
                    if cur & num == 0:
                        cur += num
                        l+=1
                        break
        return res
s = Solution()
print(s.longestNiceSubarray([1,3,8,48,10]))