from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        n,m = len(matrix),len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zeros.append((i,j))

        for i,j in zeros:
            matrix[i] = [0]*m
            for row in matrix:
                row[j] = 0

s = Solution()
m = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s.setZeroes(m)
print(m)