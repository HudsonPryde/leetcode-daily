from typing import List


def removeStones(stones: List[List[int]]) -> int:
    uf = UnionFind(
            20002
        )  # Initialize UnionFind with a large enough range to handle coordinates

    # Union stones that share the same row or column
    for x, y in stones:
        uf._union_nodes(
            x, y + 10001
        )  # Offset y-coordinates to avoid conflict with x-coordinates

    return len(stones) - uf.component_count

class UnionFind:
    def __init__(self, n):
        self.parent = [-1]*n
        self.component_count = (0)
        self.unique_nodes = (set())
    def _find(self, node):
        if node not in self.unique_nodes:
            self.component_count += 1
            self.unique_nodes.add(node)
        if self.parent[node] == -1:
            return node
        self.parent[node] = self._find(self.parent[node])
        return self.parent[node]
    def _union_nodes(self,node1,node2):
        root1 = self._find(node1)
        root2 = self._find(node2)
        if root1 == root2:
            return
        self.parent[root1] = root2
        self.component_count -= 1

print(removeStones([[3,2],[3,1],[4,4],[1,1],[0,2],[4,0]]))