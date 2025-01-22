from typing import List
def maxProfitAssignment(difficulty: List[int], profit: List[int], worker: List[int]) -> int:
  projects = list(zip(profit, difficulty))
  projects.sort()
  worker.sort()
  profit = 0
  
  while projects:
    while projects and projects[-1][1] > worker[-1]:
      projects.pop()
    if not projects:
      break
    profit += projects[-1][0]
    worker.pop()
    if not worker:
      break

  return profit

print(maxProfitAssignment([68,35,52,47,86], [67,17,1,81,3], [92,10,85,84,82]))