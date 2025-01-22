from typing import List


def maxMatrixSum(matrix: List[List[int]]) -> int:
    n = len(matrix)
    num_neg = 0
    min_num = float('inf')
    total_sum = 0
    for i in range(n):
        for j in range(n):
            num = matrix[i][j]
            if num < 0: num_neg += 1
            num = abs(num)
            min_num = min(num, min_num)
            total_sum += num
    if num_neg%2 == 1:
        return total_sum - min_num*-2
    else:
        return total_sum

print(maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]]))