from collections import defaultdict, deque
from typing import List
def getAncestors(n: int, edges: List[List[int]]) -> List[List[int]]:
  d = [0]*n
  answer = [set([]) for _ in range(n)]
  graph = defaultdict(list)

  for u, v in edges:
    graph[u].append(v)
    answer[v].add(u)
    d[v]+=1

  q = deque()
  for node in range(n):
    if not d[node]:
      q.append(node)
  
  while q:
    node = q.popleft()
    for adj in graph[node]:
      answer[adj].update(answer[node])
      d[adj] -= 1
      if not d[adj]:
        q.append(adj)

  return [sorted(list(x)) for x in answer]

print(getAncestors(9, [[8,3],[6,3],[1,6],[7,0],[8,5],[2,1],[4,0],[2,3],[0,3],[5,3],[7,4],[4,1]]))