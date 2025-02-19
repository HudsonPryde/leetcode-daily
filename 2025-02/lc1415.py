from itertools import combinations
def getHappyString(n: int, k: int) -> str:
    def helper(s:str,res:list):
        if len(s) == n:
            res.append(s)
            return
        for l in ['a','b','c']:
            if not s or s[-1] != l:
                helper(s+l, res)
    res = []
    s = ''
    helper(s,res)
    return res[k-1]

print(getHappyString(1,3))