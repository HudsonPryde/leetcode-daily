from typing import List


def countUnguarded(m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
    cells = n*m - len(walls) - len(guards)
    walls = set([tuple(x) for x in walls])
    guards_set = set([tuple(x) for x in guards])
    seen = set()
    
    for r,c in guards:
        for i in range(c+1, n):
            if (r,i) in walls or (r,i) in guards_set:
                break
            elif (r,i) not in seen:
                cells -= 1
                seen.add((r,i))
            
        for i in range(c-1, -1, -1):
            if (r,i) in walls or (r,i) in guards_set:
                break
            elif (r,i) not in seen:
                cells -= 1
                seen.add((r,i))
        for i in range(r+1, m):
            if (i,c) in walls or (i,c) in guards_set:
                break
            else:
                if (i,c) not in seen:
                    seen.add((i,c))
                    cells -= 1
        for i in range(r-1, -1, -1):
            if (i,c) in walls or (i,c) in guards_set:
                break
            else:
                if (i,c) not in seen:
                    seen.add((i,c))
                    cells -= 1
    return cells
    
    

print(countUnguarded(4,6,[[0,0],[1,1],[2,3]],[[0,1],[2,2],[1,4]]))
