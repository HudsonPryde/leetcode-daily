from collections import defaultdict, deque
from typing import List


def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    def helper(node: int, unsafe: set, safe: set, visited: set):
        if len(graph[node]) == 0:
            safe.add(node)
            return True
        if node in visited:
            unsafe.add(node)
            return False
        visited.add(node)
        for x in graph[node]:
            if x == node:
                unsafe.add(node)
                return False
            if x not in safe and x not in unsafe:
                helper(x, unsafe, safe, visited)
            if x in safe: continue
            if x in unsafe:
                unsafe.add(node)
                return False
        safe.add(node)
        return True
    
    safe = set()
    unsafe = set()
    visited = set()
    for i in range(n):
        if i in safe or i in unsafe: continue
        helper(i, unsafe, safe, visited)
    return sorted(list(safe))

    

print(eventualSafeNodes([[1,3,4,5],[],[],[],[],[2,4]]))
