from typing import List
from heapq import heappush, heappop



def minDays(grid: List[List[int]]) -> int:
    edges = {}
    connections = []
     
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                c = 0
                edges[(i,j)] = []
                if i != 0 and grid[i-1][j] == 1:
                    edges[(i,j)].append((i-1,j))
                    c += 1
                if i != m-1 and grid[i+1][j] == 1:
                    edges[(i,j)].append((i+1,j))
                    c += 1
                if j != 0 and grid[i][j-1] == 1:
                    edges[(i,j)].append((i,j-1))
                    c += 1
                if j != n-1 and grid[i][j+1] == 1:
                    edges[(i,j)].append((i,j+1))
                    c += 1
                heappush(connections, (c, (i,j)))
    vertices = list(edges.keys())

    if len(connections) <= 1:
        return len(connections)

    def walk(p: tuple, visited: set, r: tuple):
        visited.add(p)
        if len(visited) >= len(vertices)-1:
            return True
        connected = False
        for n in edges[p]:
            if n not in visited and n != r:
                if walk(n, visited, r):
                    connected = True
        return connected
    
    while connections:
        v = set([])
        k = heappop(connections)
        if not walk(k[1], v, None):
            return 0
        v = set([])
        for h in vertices:
            if h != k[1]:
                break
        if not walk(h, v, k[1]):
            return 1

    return 2

class Solution:
    dir = [[0,1],[1,0],[-1,0],[0,-1]]
    time = 0
    def findAP(self,i,j,m,n,visited,ap,parent,min_disc_time,discovery_time):
            children = 0
            visited[i][j] = 1
            discovery_time[i][j] = self.time
            min_disc_time[i][j] = self.time
            self.time += 1
            for d in self.dir:
                l,k = i+d[0], j+d[1]
                if 0 <= l < m and 0 <= k < n:
                    if visited[l][k] == -1:
                        
                        parent[l][k] = (i,j)
                        children += 1
                        self.findAP(l,k,visited,ap,parent,min_disc_time,discovery_time)
                        min_disc_time[i][j] = min(min_disc_time[i][j], min_disc_time[l][k])
                        if parent[i][j] == None and children > 1:
                            ap = True
                        if parent[i][j] != None and min_disc_time[l][k] >= discovery_time[i][j]:
                            ap = True
                    elif (l,k) != parent[i][j]:
                        min_disc_time[i][j] = min(min_disc_time[i][j], discovery_time[l][k])
    def minDaysV2(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        visited = [[x*-1 for x in j] for j in grid]
        discovery_time = [[float('inf') for _ in range(n)]]*m
        min_disc_time = [[float('inf') for _ in range(n)]]*m
        parent = [[None for _ in range(n)]]*m
        ap = False
        land = 0

        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    land += 1
                    if visited[i][j] == -1:
                        self.findAP(i,j,m,n,visited,ap,parent,min_disc_time,discovery_time)
                        islands += 1
        print(ap)
        if 0 == islands or islands > 1:
            return 0
        if land == 1:
            return 1
        if ap:
            return 1
        return 2
s = Solution
print(s.minDaysV2([[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,0,1,1]]))