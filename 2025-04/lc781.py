from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res = 0
        cnt = {}
        for a in answers:
            cnt[a] = cnt.get(a,0)+1
        for k,v in cnt.items():
            q,r = divmod(v,k+1)
            res += q*(k+1) + ((k+1) if r > 0 else 0)
        return res
        
s = Solution()
print(s.numRabbits([10,10,10]))