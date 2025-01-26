from typing import List
from collections import deque


def lexicographicallySmallestArray(nums: List[int], limit: int) -> List[int]:
    n = len(nums)
    m = sorted(nums)
    g = 0
    groups = {m[0]: 0}
    members = {0:deque([m[0]])}
    for i in range(1, n):
        if m[i]-m[i-1] > limit:
            g += 1
        groups[m[i]] = g
        if g not in members: members[g] = deque()
        members[g].append(m[i])

    for i in range(n):
        c_g = groups[nums[i]]
        nums[i] = members[c_g].popleft()

    return nums


print(lexicographicallySmallestArray([73,56,32,70,43,51,40,39,75,45], 8))