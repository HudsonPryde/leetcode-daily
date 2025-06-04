from collections import deque
from typing import List


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        boxes = deque(initialBoxes)
        locked = set()
        res = 0
        while boxes:
            box = boxes.popleft()
            if status[box]:
                res += candies[box]
                for key in keys[box]:
                    status[key] = 1
                    if key in locked:
                        boxes.append(key)
                        locked.remove(key)
                for b in containedBoxes[box]:
                    boxes.append(b)
            else:
                locked.add(box)
        return res

s = Solution()
print(s.maxCandies([1,0,1,0],[7,5,4,100],[[],[],[1],[]],[[1,2],[3],[],[]],[0]))
