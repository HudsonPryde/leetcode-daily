from typing import List
from collections import deque, defaultdict


def findDiagonalOrder(nums: List[List[int]]) -> List[int]:
    n = len(nums)
    d = deque([(0,0)])
    res = []
    while d:
        i,j = d.popleft()
        res.append(nums[i][j])

        if j == 0 and i < n-1:
            d.append((i+1,j))
        if j < len(nums[i]) - 1:
            d.append((i,j+1))
    return res

def findDiagonalOrderV2(nums: List[List[int]]) -> List[int]:
    n = len(nums)
    l = max([len(x) for x in nums])
    m = defaultdict(list)
    dig = 0
    for col in range(l):
        for row in range(n):
            if col >= len(nums[row]):
                continue
            m[col+row].append(nums[row][col])
            dig = col+row
    res = []
    for i in range(dig+1):
        res.extend(m[i])

    return res
print(findDiagonalOrderV2([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))