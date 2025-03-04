class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        return self._convert(n)
    def _convert(self,n):
        if n == 0:
            return True
        x = n%3
        n //= 3
        if x < 0:
            n += 1
        if x == 2:
            return False
        return self._convert(n)
    
s = Solution()
print(s._convert(12))