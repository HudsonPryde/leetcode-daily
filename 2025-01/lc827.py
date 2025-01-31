from typing import List


def largestIsland(grid: List[List[int]]) -> int:
    n = len(grid)
    parent = [[-1 for _ in range(n)] for _ in range(n)]
    size = {}
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]

    def helper(i,j,root):
        if parent[i][j] in size: return size[(i,j)]
        if grid[i][j] == 0: return 0
        parent[i][j] = root
        t = 1
        for k,h in dirs:
            n_i, n_j = i+k, j+h
            if not (0<=n_i<n) or not (0<=n_j<n): continue
            if parent[n_i][n_j] != -1: continue
            t += helper(n_i,n_j,root)
        return t

    res = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                t = 1
                roots = set()
                for k,h in dirs:
                    n_i, n_j = i+k, j+h
                    if not (0<=n_i<n) or not (0<=n_j<n): continue
                    if grid[n_i][n_j] == 0: continue
                    if parent[n_i][n_j] in roots: continue
                    if parent[n_i][n_j] != -1:
                        t += size[parent[n_i][n_j]]
                    else:
                        size[(n_i,n_j)] = helper(n_i,n_j,(n_i,n_j))
                        t += size[(n_i,n_j)]
                    roots.add(parent[n_i][n_j])
                res = max(res, t)
            if parent[i][j] != -1: continue
            size[(i,j)] = helper(i,j,(i,j))
            res = max(res,size[(i,j)])
    return res


print(largestIsland([[1,1,0,1],[1,0,0,1],[1,0,0,1],[1,0,0,1]]))
#[[1,1,0,1],
# [1,0,0,1],
# [1,0,0,1],
# [1,0,0,1]] 
