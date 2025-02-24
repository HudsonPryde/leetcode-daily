from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.adj = defaultdict(list)
        self.bobPath = {}
        self.visited = set()
        self.maxNet = float('-inf')
    
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        for a,b in edges:
            self.adj[a].append(b)
            self.adj[b].append(a)
        self._findBobPath(bob,0)
        self.visited.clear()
        self._findAlicePath(0,0,0,amount)
        return self.maxNet



    def _findAlicePath(self,curr:int,step:int,net:int,amount:List[int]):
        self.visited.add(curr)
        if curr not in self.bobPath or step < self.bobPath[curr]:
            net += amount[curr]
        elif step == self.bobPath[curr]:
            net += amount[curr]//2
        if len(self.adj[curr]) == 1 and curr != 0:
            self.maxNet = max(self.maxNet, net)
        for node in self.adj[curr]:
            if node in self.visited: continue
            self._findAlicePath(node,step+1,net,amount)

    
    def _findBobPath(self,curr:int,step:int):
        self.bobPath[curr] = step
        self.visited.add(curr)
        if curr == 0:
            return True
        for node in self.adj[curr]:
            if node not in self.visited and self._findBobPath(node,step+1):
                return True
        self.bobPath.pop(curr,None)
        return False

        
            
s = Solution()
print(s.mostProfitablePath([[0,1],[1,2],[1,3],[3,4]],3,[-2,4,2,-4,6]))