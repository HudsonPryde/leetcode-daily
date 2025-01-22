import math


def passThePillow(n: int, time: int) -> int:
  rounds = 0
  p = 1
  for _ in range(0, time):
    if rounds % 2 == 0:
      if p == n:
        # print(p, rounds)
        rounds += 1
        p -= 1
      else:
        p += 1
    else:
      if p == 1:
        # print(p, rounds)
        rounds += 1
        p += 1
      else:
        p -= 1
  return p

def passThePillowO1(n: int, time: int):
  r = (time%(2*n-2))
  if r >= n:
    m = r%n
    return n-m-1
  else:
    return r+1

            
print(passThePillowO1(3,1000), "expect: 1")
print(passThePillowO1(4,5), "expect: 2")
print(passThePillowO1(23,967), "expect: 2")
print(passThePillowO1(2,1000), "expect: 1")
print(passThePillowO1(18,38), "expect: 5")