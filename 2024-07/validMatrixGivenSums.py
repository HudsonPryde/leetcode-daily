from typing import List


def restoreMatrix(rowSum: List[int], colSum: List[int]) -> List[List[int]]:
    grid = [[0]*len(colSum) for _ in range(len(rowSum))]
    rowSum = list(zip(rowSum, range(len(rowSum))))
    colSum = list(zip(colSum, range(len(colSum))))
    while rowSum and colSum:
        min_row, min_col = min(rowSum), min(colSum)
        min_row_i, min_col_i = rowSum.index(min_row), colSum.index(min_col)

        if min_row[0] <= min_col[0]:
            grid[min_row[1]][min_col[1]] = min_row[0]
            colSum[min_col_i] = (min_col[0] - min_row[0], min_col[1])
            rowSum.pop(min_row_i)
        else:
            grid[min_row[1]][min_col[1]] = min_col[0]
            rowSum[min_row_i] = (min_row[0] - min_col[0], min_row[1])
            colSum.pop(min_col_i)

    return grid


restoreMatrix([1,1,6], [5,3])