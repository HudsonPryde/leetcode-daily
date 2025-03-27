from typing import List
from collections import Counter

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        c = Counter(nums)
        m = c.most_common(1)[0][0]
        d = Counter()
        for i in range(n-1):
            num = nums[i]
            d[num] += 1
            c[num] -= 1
            if self._check(c[m],d[m],i,n):
                return i
        return -1
    def _check(self,cm:int,dm:int,i:int,n:int):
        if cm <= (n-i-1)//2 or dm <= (i+1)//2:
            return False
        return True


s = Solution()
print(s.minimumIndex([1,2,1,1]))