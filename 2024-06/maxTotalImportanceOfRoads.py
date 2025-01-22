from typing import List

def maximumImportance(n: int, roads: List[List[int]]) -> int:
  d = [0]*n
  for road in roads:
    d[road[0]] += 1
    d[road[1]] += 1
  d.sort()
  total = 0
  for i in range(len(d)):
    total += d[i] * (i+1)
  print(total)
  return total


maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]])
maximumImportance(5, [[0,3],[2,4],[1,3]])
maximumImportance(3, [[0, 1], [1, 2], [0, 2]])
maximumImportance(4, [[0, 1], [1, 2], [2, 3], [3, 0]])
maximumImportance(6, [[0, 1], [0, 2], [0, 3], [1, 4], [2, 5]])
maximumImportance(7, [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 6]])
maximumImportance(8, [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7]])
