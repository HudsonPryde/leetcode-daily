from typing import List


def sumPrefixScores(words: List[str]) -> List[int]:
    scores = {}
    pre1 = {}
    def helper(n, d):
        if len(n) == 0:
            return d
        if n[0] not in d:
            d[n[0]] = {}
        return helper(n[1:], d[n[0]])
    for n in words:
        helper(n, pre1)
    
    def solve(n, d, a):
        t = a+n[:1]
        if len(n) == 0:
            return
        if n[0] not in d:
            return
        scores[t] = scores.get(t, 0)+1
        return solve(n[1:], d[n[0]], t)
    
    for n in words:
        solve(n, pre1, '')
    
    res = []
    for w in words:
        score = 0
        for i in range(1,len(w)+1):
            if w[:i] in scores:
                score += scores[w[:i]]
            else:
                break
        res.append(score)

    return res

print(sumPrefixScores(["abc","ab","bc","b"]))