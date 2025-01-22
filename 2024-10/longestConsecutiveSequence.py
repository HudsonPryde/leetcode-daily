from typing import List


def longestConsecutive(nums: List[int]) -> int:
    m = {v:v for v in nums}
    k = {v:1 for v in nums}
    
    def find_set(v):
        if v == m[v]:
            return v
        m[v] = find_set(m[v])
        return m[v]
    
    def union_sets(a, b):
        a = find_set(a)
        b = find_set(b)
        if a != b:
            if k[a] < k[b]:
                a,b = b,a
            m[b] = a
            k[a] += k[b]
    for n in nums:
        if n-1 in m:
            union_sets(n, n-1)
    return max(k.values())


print(longestConsecutive([100,4,200,1,3,2]))