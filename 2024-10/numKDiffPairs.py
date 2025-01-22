from typing import List


def findPairs(nums: List[int], k: int) -> int:
    nums.sort()
    m = set()
    c = set()
    for num in nums:
        t1 = num-k
        if t1 in m:
            if abs(num-t1) == k:
                c.add((num,t1))
        t2 = -k-num
        if t2 in m:
            if abs(num-t2) == k:
                c.add((num, t2))
        m.add(num)
    return len(c)

print(findPairs([3,1,4,1,5], 2))