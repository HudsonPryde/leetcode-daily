from math import factorial


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        res = 0
        start = 10**((n-1)//2)
        stop = start*10
        d = set()
        skip = n&1
        for i in range(start,stop):
            num_ = str(i)
            num_ += num_[::-1][skip:]
            p = int(num_)
            if p%k == 0:
                d.add("".join(sorted(num_)))
        f = [factorial(i) for i in range(n+1)]
        res = 0
        for s in d:
            cnt = [0]*10
            for c in s:
                cnt[int(c)] += 1
            t = (n-cnt[0])*f[n-1]
            for x in cnt:
                t //= f[x]
            res += t
        return res
s = Solution()
print(s.countGoodIntegers(5,6))