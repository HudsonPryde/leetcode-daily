from collections import defaultdict
from typing import List
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqs = defaultdict(int)
        max_freq = 0
        num_v = 0
        for v in nums:
            freqs[v] += 1
            if max_freq < freqs[v]:
                max_freq = freqs[v]
                num_v = 1
            elif max_freq == freqs[v]:
                num_v += 1
        return num_v*max_freq