from typing import List


def averageWaitingTime(customers: List[List[int]]) -> float:
  wait_time = 0
  start_time = customers[0][0]
  for c in customers:
    if c[0] > start_time:
      start_time = c[0]
    finish_time = start_time + c[1]
    wait_time += finish_time - c[0]
    start_time = finish_time
  return wait_time/len(customers)

print(averageWaitingTime([[1,2],[2,5],[4,3]]), " expect: 5.00000")
print(averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]), " expect 3.25000")
print(averageWaitingTime([[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]]), " expect 4.16667")