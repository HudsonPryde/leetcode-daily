from typing import List


def generateMatrix(n: int) -> List[List[int]]:
    m = [[0 for _ in range(n)] for _ in range(n)]
    pos = [0,0]
    i = 1
    d = 0
    while i <= n*n:
        m[pos[0]][pos[1]] = i
        if d == 0:
            if pos[1]+1 >= n or m[pos[0]][pos[1]+1] != 0:
                d = (d+1)%4
            else:
                pos[1] += 1
                i+=1
                continue
        if d == 1:
            if pos[0]+1 >= n or m[pos[0]+1][pos[1]] != 0:
                d = (d+1)%4
            else:
                pos[0]+=1
                i+=1
                continue
        if d == 2:
            if pos[1]-1 < 0 or m[pos[0]][pos[1]-1] != 0:
                d = (d+1)%4
            else:
                pos[1]-=1
                i+=1
                continue
        if d == 3:
            if pos[0]-1 < 0 or m[pos[0]-1][pos[1]] != 0:
                d = (d+1)%4
            else:
                pos[0]-=1
                i+=1
                continue
        if i == n*n:
            break
    return m

print(generateMatrix(3))
