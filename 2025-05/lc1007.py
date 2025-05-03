from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        num1 = tops[0]
        num2 = bottoms[0]
        t,b = 0,0
        valid = True
        for i in range(n):
            if tops[i] == num1 and bottoms[i] == num1:
                continue
            elif tops[i] == num1:
                t += 1
            elif bottoms[i] == num1:
                b += 1
            else:
                valid = False
                break
        if valid:
            return min(t,b)
        t,b = 0,0
        valid = True
        for i in range(n):
            if tops[i] == num2 and bottoms[i] == num2:
                continue
            elif tops[i] == num2:
                t += 1
            elif bottoms[i] == num2:
                b += 1
            else:
                valid = False
                break
        if valid:
            return min(t,b)
        else:
            return -1

s = Solution()
print(s.minDominoRotations([2,1,2,4,2,2],[5,2,6,2,3,2]))