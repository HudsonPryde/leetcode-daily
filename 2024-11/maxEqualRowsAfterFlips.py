from typing import List


def maxEqualRowsAfterFlips(matrix: List[List[int]]) -> int:
    n = len(matrix)
    bits = {}
    max_inverse = 0
    for i in range(n):
        mask = "".join([str(x) for x in matrix[i]])
        bit_mask = int(mask,2)
        inverse_mask = bit_mask ^ int("1"*len(mask), 2)
        bits[inverse_mask] = bits.get(inverse_mask, 0) + 1
        max_inverse = max(max_inverse, bits[inverse_mask])
        bits[bit_mask] = bits.get(bit_mask, 0) + 1
        max_inverse = max(max_inverse, bits[bit_mask])
    return max_inverse

print(maxEqualRowsAfterFlips([[0,1],[1,0]]))
# 0, 1
# 1, 0