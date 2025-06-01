
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        a = self._helper(n+2)
        b = 3*self._helper(n-limit+1)
        c = 3*self._helper(n-(limit+1)*2+2)
        d = self._helper(n-3*(limit+1)+2)
        return a-b+c-d
    def _helper(self, x:int):
        return 0 if x < 0 else (x*(x-1))//2

s = Solution()
print(s.distributeCandies(6,1))