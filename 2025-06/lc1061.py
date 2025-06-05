class Solution:
    def __init__(self):
        self._parents = {l:l for l in 'abcdefghijklmnopqrstuvwxyz'}
    
    def find(self, u):
        while u != self._parents[u]:
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u
    
    def connected(self, u, v):
        return self.find(u) == self.find(v)

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return True
        if root_u < root_v:
            self._parents[root_v] = root_u
        else:
            self._parents[root_u] = root_v
        return False

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        for u,v in zip(s1,s2):
            self.union(u,v)
        return "".join([self.find(c) for c in baseStr])

s = Solution()
print(s.smallestEquivalentString("parker","morris","parser"))