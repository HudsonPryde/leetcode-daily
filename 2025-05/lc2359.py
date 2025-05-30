from typing import List


class Solution:
    def __init__(self):
        self.res = -1
        self.min_dist = float('inf')
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        d = [-1]*n
        self._helper(node1, 0, edges, d, set())
        self._helper(node2, 0, edges, d, set())
        return self.res
    def _helper(self, node: int, dist: int, edges: List[int], d: List[int], seen: set):
        if node in seen:
            return
        if d[node] == -1:
            d[node] = dist
        else:
            max_dist = max(dist, d[node])
            if max_dist < self.min_dist:
                self.res = node
                self.min_dist = max_dist
            elif max_dist == self.min_dist:
                self.res = min(self.res, node)
        d[node] = max(d[node], dist)
        if edges[node] == -1:
            return
        seen.add(node)
        self._helper(edges[node], dist+1, edges, d, seen)

s = Solution()
print(s.closestMeetingNode([2,2,3,-1], 0, 1))