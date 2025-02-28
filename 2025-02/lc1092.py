class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if str1 == str2: return str1
        m,n = len(str1),len(str2)
        memo = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        lcs = self._lcs(str1,str2,m,n,memo)
        res = ''
        prev1,prev2 = 0,0
        for l in lcs:
            idx1,idx2 = str1.find(l,prev1),str2.find(l,prev2)
            res += str1[prev1:idx1] + str2[prev2:idx2] + l
            prev1,prev2 = idx1+1,idx2+1
        res += str1[prev1:] + str2[prev2:]
        return res
    def _lcs(self,s1,s2,m,n,memo):
        if m == 0 or n == 0:
            return ''
        if memo[m][n] != -1:
            return memo[m][n]
        if s1[m-1] == s2[n-1]:
            memo[m][n] =  self._lcs(s1,s2,m-1,n-1,memo) + s2[n-1]
            return memo[m][n]
        memo[m][n] = max(self._lcs(s1,s2,m,n-1,memo), self._lcs(s1,s2,m-1,n,memo),key=lambda x: len(x))
        return memo[m][n]
    
s = Solution()
print(s.shortestCommonSupersequence("hjfjkweoinvoiwwef","oilkoliseuhkncewoi"))