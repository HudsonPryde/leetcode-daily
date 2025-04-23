class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = {}
        m = 0
        for i in range(1,n+1):
            t = self._helper(i)
            d[t] = d.get(t,0)+1
            m = max(d[t],m)
        return list(d.values()).count(m)

    def _helper(self,num:int):
        total = 0
        while num > 0:
            num, res = divmod(num,10)
            total += res
        return total
    
s = Solution()
print(s.countLargestGroup(13))