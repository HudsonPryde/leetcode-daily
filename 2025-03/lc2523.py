from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [True for _ in range(right+1)]
        num1, num2 = 0,0
        p = 2
        while (p*p <= right):
            if primes[p] == True:
                for i in range(p*p,right+1,p):
                    primes[i] = False
            p += 1

        prev = 0
        for i in range(max(left,2), right+1):
            if not primes[i]: continue
            if prev != 0:
                if num1 == 0 and num2 == 0:
                    num1,num2 = prev,i
                elif i-prev < num2-num1:
                    num1,num2 = prev,i
            prev = i

        return [num1,num2] if min([num1,num2]) != 0 else [-1,-1]

s = Solution()
print(s.closestPrimes(19,31))