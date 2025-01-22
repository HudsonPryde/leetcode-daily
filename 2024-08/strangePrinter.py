from functools import cache
from itertools import groupby

class Solution:
    def strangePrinter1(self, s: str) -> int:
        @cache
        def f(i, j):
            if i==j: return 1
            if s[i]==s[j]: return f(i, j-1)
            ans=f(i, j-1)+1
            k=i+1
            while k<j-1:
                if s[k]==s[j]:
                    ans=min(ans, f(i, k-1)+f(k, j-1))
                    k+=1
                k+=1
            return ans
        s=[c for c, _ in groupby(s)]
        return f(0, len(s)-1)
    def helper(self, s: str):
        idx = 1
        while idx < len(s):
            if s[idx] == s[idx-1]:
                s = s[:idx] + s[idx+1:]
            else:
                idx += 1
        return s
    def strangePrinter2(self, s: str):
        a = self.helper(s)
        n = len(a)
        h = {}
        t = [n] * n
        for i in reversed(range(n)):
            if a[i] in h:
                t[i] = h[a[i]]
            h[a[i]] = i
        d = [[0] * n for _ in range(n + 1)]
        for i in range(n):
            d[i][i] = 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                d[i][j] = 1 + d[i + 1][j]
                k = t[i]
                while k <= j:
                    d[i][j] = min(d[i][j], d[i][k - 1] + d[k + 1][j])
                    k = t[k]
        return d[0][n - 1]

s= Solution()
print(s.strangePrinter1("tgbtbg"))
