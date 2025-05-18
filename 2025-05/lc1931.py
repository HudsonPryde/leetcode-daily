
MOD = 10**9+7

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        cols = []
        for c in range(3):
            self._gen_cols(cols, [c], m)
        
        dp = [[None]*n for _ in range(len(cols))]
        res = 0
        for i,c in enumerate(cols):
            res = (res + self._helper(i, 1, cols, n, dp)) % MOD
        return res
        
    def _gen_cols(self, cols: list[list[int]], col: list[int], m: int):
        if len(col) == m:
            cols.append(col)
            return
        for c in range(3):
            if c != col[-1]:
                self._gen_cols(cols, col+[c], m)
    
    def _helper(self, prev: int, idx: int, cols: list[list[int]], n:int, dp: list[list[int]]):
        if idx == n:
            return 1
        if dp[prev][idx] != None:
            return dp[prev][idx]
        cnt = 0
        for i,c in enumerate(cols):
            if i == prev: continue
            if self._check_valid(c,cols[prev]):
                cnt = (cnt + self._helper(i, idx+1, cols, n, dp)) % MOD
        dp[prev][idx] = cnt
        return dp[prev][idx]
    
    def _check_valid(self, a: list[int], b:list[int]) -> bool:
        for u,v in zip(a,b):
            if u==v: return False
        return True
        
        


s = Solution()
print(s.colorTheGrid(5,1000))

