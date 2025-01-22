from typing import List


def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    visited = [[rStart,cStart]]
    pos = [rStart,cStart]
    i = 1
    while len(visited) < rows*cols:
        # right then down
        if i % 2 == 1:
            for _ in range(i):
                pos[1]+=1
                if (0 <= pos[0] < rows) and (0 <= pos[1] < cols):
                    visited.append([pos[0], pos[1]])
            for _ in range(i):
                pos[0]+=1
                if (0 <= pos[0] < rows) and (0 <= pos[1] < cols):
                    visited.append([pos[0], pos[1]])
        # left then up
        else:
            for _ in range(i):
                pos[1]-=1
                if (0 <= pos[0] < rows) and (0 <= pos[1] < cols):
                    visited.append([pos[0], pos[1]])
            for _ in range(i):
                pos[0]-=1
                if (0 <= pos[0] < rows) and (0 <= pos[1] < cols):
                    visited.append([pos[0], pos[1]])
        i += 1
    return visited

print(spiralMatrixIII(1,4,0,0))