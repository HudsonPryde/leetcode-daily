from typing import List
from collections import Counter
import math


def threeSumMulti(arr: List[int], target: int) -> int:
    c = Counter(arr)
    arr = list(set(arr))
    n = len(arr)
    arr.sort()
    res = 0
    for i in range(n):
        for j in range(i, n):
            diff = target - arr[i] - arr[j]
            if diff < arr[i] or diff < arr[j]:
                break
            if arr[i] == arr[j] == diff:
                res += math.comb(c[arr[i]], 3)
            elif arr[i] == arr[j] and diff in c:
                res += math.comb(c[arr[i]], 2)*c[diff]
            elif arr[j] == diff:
                res += math.comb(c[arr[j]], 2)*c[arr[i]]
            elif arr[i] == diff:
                res += math.comb(c[arr[i]], 2)*c[arr[j]]
            elif diff in c:
                res += c[arr[i]]*c[arr[j]]*c[diff]
    return res
print(threeSumMulti([1,1,2,2,3,3,4,4,5,5], 8))
# 5, 5, ,5 ,5