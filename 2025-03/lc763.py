from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_idx = {}
        for i,l in enumerate(s):
            end_idx[l] = i
        res = []
        cur_l = 0
        cur_e = 0
        for i,l in enumerate(s):
            cur_l += 1
            if end_idx[l] > cur_e: cur_e = end_idx[l]
            if cur_e == i:
                res.append(cur_l)
                cur_l = 0
                cur_e = 0
        return res

s = Solution()
print(s.partitionLabels("eccbbbbdec"))