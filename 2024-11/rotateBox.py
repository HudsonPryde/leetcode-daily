from typing import List


def rotateTheBox(box: List[List[str]]) -> List[List[str]]:
    n,m = len(box), len(box[0])
    flip = [['.']*n for _ in range(m)]
    
    for row in range(n):
        stable = m-1
        for i in range(m-1,-1,-1):
            if box[row][i] == "#":
                flip[stable][-row-1] = "#"
                stable -= 1
            elif box[row][i] == "*":
                flip[i][-row-1] = "*"
                stable = i-1
    return flip

print(rotateTheBox([["#","#","#",".",".","."],["#","#","#",".",".","."],["#","#","#",".",".","."],["#","#","#",".",".","."],["#","#","#",".",".","."]]))
