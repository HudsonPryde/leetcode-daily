from typing import List
def minMovesToSeat(seats: List[int], students: List[int]) -> int:
  seats.sort()
  students.sort()
  o = 0
  for seat, student in zip(seats, students):
    o += abs(seat - student)
  return o
print(minMovesToSeat([3,1,5], [2,7,4]))