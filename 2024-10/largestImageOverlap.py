from typing import List


def largestOverlap(img1: List[List[int]], img2: List[List[int]]) -> int:
    n = len(img1)
    pairs = {}
    max_over = 0
    m1 = [(i,j)  for i in range(n) for j in range(n) if img1[i][j] == 1]
    m2 = [(i,j)  for i in range(n) for j in range(n) if img2[i][j] == 1]
    for i in range(len(m1)):
        for j in range(len(m2)):
            offset = (m2[j][0]-m1[i][0], m2[j][1]-m1[i][1])
            pairs[offset] = pairs.get(offset, 0)+1
            max_over = max(pairs[offset], max_over)
    return max_over

print(largestOverlap([[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]], [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,0]]))