from collections import defaultdict
from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        d=set(arr)
        maxLen = 0
        currLen = 0
        n = len(arr)
        for i in range(n):
            for j in range(i+1,n):
                currLen = 0
                a,b = arr[i],arr[j]
                while a+b in d:
                    a,b = b,a+b
                    currLen = 3 if currLen == 0 else currLen+1
                maxLen = max(maxLen,currLen)
        return maxLen

s = Solution()
print(s.lenLongestFibSubseq([1,3,7,11,12,14,18]))