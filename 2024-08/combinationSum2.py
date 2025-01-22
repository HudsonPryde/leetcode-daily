from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    res = []
    
    def solve(i: int, cur: List[int], k: int):
        if k == 0:
            res.append(cur.copy())
            return
        for n in range(i, len(candidates)):
            if n>i and candidates[n] == candidates[n-1]: continue
            if candidates[n] > k: break
            
            cur.append(candidates[n])
            solve(n+1, cur, k-candidates[n])
            cur.pop()
    
    solve(0, [], target)
    return res

print(combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2],7))