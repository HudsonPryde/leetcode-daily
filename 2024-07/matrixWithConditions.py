from typing import List


def buildMatrix(k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
    m = [[0]*k for _ in range(k)]
    g = {i: {'x':0,'y':0,'row':[],'col':[]} for i in range(1, k+1)}
    for c in rowConditions:
        g[c[1]]['row'].append(c)
    for c in colConditions:
        g[c[1]]['col'].append(c)
    
    r_visited = [False for _ in range(k)]
    r_stack = []
    
    def checkRowCondition(value: int):
        if r_visited[value-1]:
            if value not in r_stack:
                return False
            return True
        r_visited[value-1] = True
        for v in g[value]['row']:
            if not checkRowCondition(v[0]):
                return False
        
        r_stack.append(value)
        return True
    
    for i in range(1, k+1):
        if not checkRowCondition(i):
            return []

    c_visited = [False for _ in range(k)]
    c_stack = []

    def checkColCondition(value: int):
        if c_visited[value-1]:
            if value not in c_stack:
                return False
            return True
        c_visited[value-1] = True
        for v in g[value]['col']:
            if not checkColCondition(v[0]):
                return False
        
        c_stack.append(value)
        return True
    
    for i in range(1, k+1):
        if not checkColCondition(i):
            return []
        
    for i,v in enumerate(zip(r_stack,c_stack)):
        g[v[0]]['x'] = i
        g[v[1]]['y'] = i
    
    for k,v in g.items():
        m[v['x']][v['y']] = k

    return m

print(buildMatrix(3, [[1,2],[3,2]], [[2,1],[3,2]]))
print(buildMatrix(3, [[1,2],[2,3],[3,1],[2,3]], [[2,1]]))