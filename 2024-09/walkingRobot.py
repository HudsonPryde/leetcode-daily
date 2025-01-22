from typing import List


def robotSim(commands: List[int], obstacles: List[List[int]]) -> int:
    o = {(a,b):True for a,b in obstacles}
    x,y=0,0
    d = 0
    res = 0
    for c in commands:
        if c < 0:
            if c == -2:
                d = (d-1) % 4
            else:
                d = (d+1) % 4
        else:
            for _ in range(c):
                if d == 0:
                    if (x,y+1)  not in o:
                        y+=1
                elif d == 1:
                    if (x+1,y) not in o:
                        x+=1
                elif d == 2:
                    if (x,y-1) not in o:
                        y-=1
                elif d == 3:
                    if (x-1,y) not in o:
                        x-=1
            res = max(res, (x**2 + y**2))
    return res

print(robotSim([4,-1,3],[[1,2]]))