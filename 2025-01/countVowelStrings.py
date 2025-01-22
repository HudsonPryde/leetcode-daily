from typing import List


def vowelStrings(words: List[str], queries: List[List[int]]) -> List[int]:
    vowels = ['a','e','i','o','u']
    def helper(s: str):
        return 1 if s[0] in vowels and s[-1] in vowels else 0
    v = [helper(words[0])]
    
    for i in range(1, len(words)):
        v.append(v[i-1]+helper(words[i]))
    
    res = []
    for i in range(len(queries)):
        a,b = queries[i]
        if a > 0:
            q = v[b]-v[a-1]
        else:
            q = v[b]
        res.append(q)
    return res

print(vowelStrings(["aba","bcb","ece","aa","e"], [[0,2],[1,4],[1,1]]))
