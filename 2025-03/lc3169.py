from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        prev = None
        for start,end in meetings:
            if prev == None:
                days -= (end-start)+1
                prev = (start,end)
                continue
            prev_start,prev_end = prev
            if end <= prev_end: continue
            if start > prev_end:
                days -= (end-start)+1
                prev = (start,end)
                continue
            elif end > prev_end:
                days -= (end-prev_end)
                prev = (prev_start,end)
                continue
        return days
s =Solution()
print(s.countDays(6,[[1,6]]))

