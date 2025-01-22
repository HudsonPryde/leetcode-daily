def maximumGain(s: str, x: int, y: int) -> int:
  stack = []
  total = 0

  
  for n in s:
    if stack and n == "b" and stack[-1] == "a" and x > y:
      total += x
      stack.pop()
    elif stack and n == "a" and stack[-1] == "b" and y > x:
      total += y
      stack.pop()
    else:
      stack.append(n)
  s = "".join(stack)
  stack = []
  
  for n in s:
    if stack and n == "b" and stack[-1] == "a":
      total += x
      stack.pop()
    elif stack and n == "a" and stack[-1] == "b":
      total += y
      stack.pop()
    else:
      stack.append(n)
  
  return total
      


print(maximumGain("aabbaaxybbaabb", 5, 4))