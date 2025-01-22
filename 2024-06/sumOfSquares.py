import math

def judgeSquareSum(c: int) -> bool:
  l, r = 0, int(math.sqrt(c))

  while l <= r:
    l_num = l**2
    r_num = r**2

    if l_num + r_num == c:
      return True
    elif l_num + r_num < c:
      l += 1
    else:
      r -= 1

print(judgeSquareSum(5))