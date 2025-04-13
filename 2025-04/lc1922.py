class Solution:
    def __init__(self):
        self.MOD = 10**9+7
    def countGoodNumbers(self, n: int) -> int:
        return self._helper(5, (n+1)//2)*self._helper(4,n//2)%self.MOD
    def _helper(self, x:int, e:int):
        t, m = 1, x
        while e > 0:
            if e % 2 == 1:
                t = t * m % self.MOD
            m = m * m % self.MOD
            e //= 2
        return t
    
s =Solution()
print(s.countGoodNumbers(100000000))
