from typing import List


def luckyNumbers (matrix: List[List[int]]) -> List[int]:
    lucky_nums = []
    for row in range(len(matrix)):
        v_min = min(matrix[row])
        i_min = matrix[row].index(v_min)
        if max([y[i_min] for y in matrix]) == v_min:
            lucky_nums.append(v_min)
    return lucky_nums

print(luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))