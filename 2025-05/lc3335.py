
from typing import Counter


MOD = 1_000_000_007
dp = [1]*(100_000 + 26)
for i in range(26, len(dp)):
    dp[i] = (dp[i-26]+dp[i-25]) % MOD

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        res = 0
        c = Counter(s)
        for k,v in c.items():
            res = (res + v * dp[(ord(k)-97)+t]) % MOD
        return res