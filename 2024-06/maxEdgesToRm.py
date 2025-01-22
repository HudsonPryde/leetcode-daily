from collections import defaultdict
from typing import List

class Disjoint:
  def __init__(self, size):
    self.parent = list(range(size))
    self.size = [1] * size
  
  def make_set(self, element):
     index = element
     self.parent[index] = -1
  
  def find(self, element):
     if self.parent[element] == element:
        return element
     self.parent[element] = self.find(self.parent[element])
     return self.parent[element]
  
  def union(self, element1, element2):
     root1 = self.find(element1)
     root2 = self.find(element2)
     if root1 != root2:
        if self.size[root1] < self.size[root2]:
           self.parent[root1] = root2
           self.size[root2] += self.size[root1]
        else:
           self.parent[root2] = root1
           self.size[root1] += self.size[root2]
  
  def same_set(self, element1, element2):
     return self.find(element1) == self.find(element2)

  

def maxNumEdgesToRemove(n: int, edges: List[List[int]]) -> int:
  a_span, b_span = Disjoint(n+1), Disjoint(n+1)

  num_edges = 0
  edges.sort(reverse=True)
  for t, u, v in edges:
      edge_used = False
      if (t == 3 or t == 2) and not b_span.same_set(u, v):
          edge_used = True
          b_span.union(u, v)
      
      if (t == 3 or t == 1) and not a_span.same_set(u, v):
          edge_used = True
          a_span.union(u, v)
      
      if edge_used: num_edges += 1
      
      if a_span.size[a_span.find(u)] == n and b_span.size[b_span.find(u)] == n:
          return len(edges) - (num_edges)


  return -1

print(maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))
print(maxNumEdgesToRemove(13, [[1,1,2],[2,1,3],[3,2,4],[3,2,5],[1,2,6],[3,6,7],[3,7,8],[3,6,9],[3,4,10],[2,3,11],[1,5,12],[3,3,13],[2,1,10],[2,6,11],[3,5,13],[1,9,12],[1,6,8],[3,6,13],[2,1,4],[1,1,13],[2,9,10],[2,1,6],[2,10,13],[2,2,9],[3,4,12],[2,4,7],[1,1,10],[1,3,7],[1,7,11],[3,3,12],[2,4,8],[3,8,9],[1,9,13],[2,4,10],[1,6,9],[3,10,13],[1,7,10],[1,1,11],[2,4,9],[3,5,11],[3,2,6],[2,1,5],[2,5,11],[2,1,7],[2,3,8],[2,8,9],[3,4,13],[3,3,8],[3,3,11],[2,9,11],[3,1,8],[2,1,8],[3,8,13],[2,10,11],[3,1,5],[1,10,11],[1,7,12],[2,3,5],[3,1,13],[2,4,11],[2,3,9],[2,6,9],[2,1,13],[3,1,12],[2,7,8],[2,5,6],[3,1,9],[1,5,10],[3,2,13],[2,3,6],[2,2,10],[3,4,11],[1,4,13],[3,5,10],[1,4,10],[1,1,8],[3,3,4],[2,4,6],[2,7,11],[2,7,10],[2,3,12],[3,7,11],[3,9,10],[2,11,13],[1,1,12],[2,10,12],[1,7,13],[1,4,11],[2,4,5],[1,3,10],[2,12,13],[3,3,10],[1,6,12],[3,6,10],[1,3,4],[2,7,9],[1,3,11],[2,2,8],[1,2,8],[1,11,13],[1,2,13],[2,2,6],[1,4,6],[1,6,11],[3,1,2],[1,1,3],[2,11,12],[3,2,11],[1,9,10],[2,6,12],[3,1,7],[1,4,9],[1,10,12],[2,6,13],[2,2,12],[2,1,11],[2,5,9],[1,3,8],[1,7,8],[1,2,12],[1,5,11],[2,7,12],[3,1,11],[3,9,12],[3,2,9],[3,10,11]]))
print("expect: 114")
print(maxNumEdgesToRemove(4, [[3,1,2], [3,3,4], [1,1,3],[2,2,4]]))

def altMethod(n: int, edges: List[List[int]]) -> int:
    a_span, b_span = [-1]*(n+1), [-1]*(n+1)

    def find(span, node):
        if span[node] < 0:
            return node
        span[node] = find(span, span[node])
        return span[node]

    num_removed = 0

    for t, u, v in edges:
        if t == 3:
            u_span = find(a_span, u)
            v_span = find(a_span, v)

            if u_span != v_span:
                a_span[u_span] += a_span[v_span]
                a_span[v_span] = u_span
            else:
                num_removed += 1
    
    b_span = a_span.copy()
    for t, u, v in edges:
        if t == 1:
            u_span = find(a_span, u)
            v_span = find(a_span, v)
            if u_span != v_span:
                a_span[u_span] += a_span[v_span]
                a_span[v_span] = u_span
            else:
                num_removed += 1
        if t == 2:
            u_span = find(b_span, u)
            v_span = find(b_span, v)
            if u_span != v_span:
                b_span[u_span] += b_span[v_span]
                b_span[v_span] = u_span
            else:
                num_removed += 1
    al, bl = min(a_span), min(b_span)
    if (al == bl and al == -1*n):
        return num_removed
    else:
        return -1

         
print(altMethod(4, [[3,1,2], [3,3,4], [1,1,3],[2,2,4]]))