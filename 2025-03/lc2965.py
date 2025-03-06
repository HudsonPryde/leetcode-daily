from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        arr = [0 for _ in range(n**2)]
        for r in grid:
            for c in r:
                arr[c-1] += 1
        return [arr.index(2)+1, arr.index(0)+1]