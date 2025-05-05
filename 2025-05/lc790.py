MOD = 10**9 + 7
res = [1,2,5,11]
for i in range(4,1001):
    num = ((res[i-1]*2)+(res[i-3]))%MOD
    res.append(num)

class Solution:
    def numTilings(self, n: int) -> int:
        return res[n-1]

s = Solution()
print(s.numTilings(8))