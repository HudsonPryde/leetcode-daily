from typing import List
from bisect import bisect_right


def isArraySpecial(nums: List[int], queries: List[List[int]]) -> List[bool]:
    nums.append(nums[-1])
    n = len(nums)
    # precompute alternating parity ranges
    ends = []
    starts = []
    slow = 0
    for i in range(1, n):
        # slow is the start of the potential range
        if nums[i]%2 == nums[i-1]%2:
            # range is not alternating
            if i-slow > 1:
                ends.append(i-1)
                starts.append(slow)
            slow = i

    res = []
    for q in queries:
        if q[0] == q[1]:
            res.append(True)
            continue
        if not starts:
            res.append(False)
            continue
        i = bisect_right(starts, q[0])-1
        r = [starts[i],ends[i]]
        if q[0] >= r[0] and q[1] <= r[1]:
            res.append(True)
        else:
            res.append(False)
    return res

print(isArraySpecial([2,7,1,1,8,9], [[3,4]]))