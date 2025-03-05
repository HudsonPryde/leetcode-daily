class Solution:
    def coloredCells(self, n: int) -> int:
        res = 0
        for i in range(n):
            res += 2**i
        return res