from typing import Counter, List

MOD = 1_000_000_007


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        m1 = [[0]*26 for _ in range(26)]
        for l in s:
            m1[ord(l)-97][ord(l)-97] += 1
        m2 = []
        for i in range(26):
            x = [0]*26
            for j in range(1,nums[i]+1):
                x[(i+j)%26] = 1
            m2.append(x)
        res = self.power(m2, t)
        res = [sum(x)%MOD for x in res]
        total = 0
        c = Counter(s)
        for k,v in c.items():
            total = (total + v*res[ord(k)-97])%MOD
        return total%MOD
        
    def multiply(self, A, B):
        # Matrix to store the result
        C = [[0]*26 for _ in range(26)]
        for i in range(26):
            for j in range(26):
                for k in range(26):
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j])%MOD

        # Copy the result back to the first matrix A
        for i in range(26):
            for j in range(26):
                A[i][j] = C[i][j]

    def power(self, M, expo):
        # Initialize result with identity matrix
        ans = [[0]*26 for _ in range(26)]
        for i in range(26):
            ans[i][i] += 1

        # Fast Exponentiation
        while expo > 0:
            if expo & 1:
                self.multiply(ans, M)
            self.multiply(M, M)
            expo >>= 1

        return ans





s = Solution()
print(s.lengthAfterTransformations("k",2,[2,2,1,3,1,1,2,3,3,2,1,2,2,1,1,3,1,2,2,1,3,3,3,2,2,1]))