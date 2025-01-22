from typing import List


def maxChunksToSorted(arr: List[int]) -> int:
    n = len(arr)
    res = 0
    target = set() # to keep track of the nums we should have seen to sort everything
    seen = set() # to keep track of all nums weve seen so far
    for i in range(n):
        target.add(i)
        seen.add(arr[i])
        if target == seen:
            res += 1
    return res

print(maxChunksToSorted([1, 2, 0, 3, 5, 4]))