def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
  cells = [[],[],[]]
  for i in range(N):
    if C[i] == "P":
      cells[0].append(i)
    elif C[i] == 'A':
      cells[1].append(i)
    elif C[i] == 'B':
      cells[2].append(i)
  res = 0
  for j in cells[0]:
    for h in cells[1]:
      if h < j:
        if X <= abs(h-j) <= Y:
          for k in cells[2]:
            if k < h:
              if X <= abs(k-h) <= Y:
                res += 1
      if h > j:
        if X <= abs(h-j) <= Y:
          for k in cells[2]:
            if k > h:
              if X <= abs(k-h) <= Y:
                res += 1
  return res

print(getArtisticPhotographCount(8,'.PBAAP.B',1,3))