from typing import List
from itertools import combinations


def countMaxOrSubsets(nums: List[int]) -> int:
    max_or = 0
    for num in nums:
        max_or = max_or|num
    res = 0
    for i in range(len(nums)+1):
        for c in combinations(nums, i):
            t = 0
            for n in c:
                t = t|n
                if t == max_or:
                    res += 1
                    break

    return res

print(countMaxOrSubsets([1,2,3,7]))
# [7], [1,7], [2,7], [3,7], [1,2,7], [1,3,7], [2,3,7], [1,2,3,7]


    