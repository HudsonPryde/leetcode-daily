from collections import defaultdict
from typing import List


def maximumSum(nums: List[int]) -> int:
    def helper(n: int):
        s = 0
        while n:
            s += n % 10
            n //= 10
        return s
    res = -1
    d = {}
    for num in nums:
        t = helper(num)
        if t in d:
            if len(d[t]) < 2:
                d[t].append(num)
            else:
                if d[t][1] < num:
                    d[t][1] = num
                elif d[t][0] < num:
                    d[t][0] = num
            d[t].sort(reverse=True)
            k = sum(d[t])
            if k > res:
                res = k
        else:
            d[t] = [num]
    return res

print(maximumSum([18,43,36,13,7]))