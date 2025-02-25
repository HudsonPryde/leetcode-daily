from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = 0
        numOdd = 0
        numEven = 1
        currSum = 0
        for num in arr:
            currSum += num
            if currSum%2 == 0:
                res += numOdd
                numEven += 1
            elif currSum%2 == 1:
                res += numEven
                numOdd += 1
        return res%((10**9)+7)


s = Solution()
print(s.numOfSubarrays([1,2,3,4,5,6,7]))