from typing import List
from collections import defaultdict


def minimumSubarrayLength(nums: List[int], k: int) -> int:
    l = 0
    c = nums[0]
    freq = defaultdict(int)
    min_len = len(nums)+1
    for i in range(len(nums)):
        c = c|nums[i]
        b = bin(nums[i])[:1:-1]
        for j in range(len(b)):
            if b[j] == "1": freq[j] += 1
        if c >= k:
            min_len = min(min_len, i-l+1)
            p = list(bin(c)[:1:-1])
            while c >= k and l < i:
                # remove nums[l] from window
                b = bin(nums[l])[:1:-1]
                for j in range(len(b)):
                    if b[j] == "1": freq[j] -= 1
                    if freq[j] == 0: p[j] ="0"
                c = int("".join(p[::-1]), 2)
                if c >= k: min_len = min(min_len, i-l)
                l += 1
    if min_len > len(nums): return -1
    else: return min_len

print(minimumSubarrayLength([2,1,8], 10))