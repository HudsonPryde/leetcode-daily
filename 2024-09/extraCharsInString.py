from typing import List


def minExtraChar(s: str, dictionary: List[str]) -> int:
    n = len(s)
    word_set = set(dictionary)
    mem = [-1] * (n + 1)
    def helper(i):
        if i == n:
            return 0
        if mem[i] != -1:
            return mem[i]
        min_extra = 1 + helper(i + 1)
        for j in range(i, n + 1):
            if s[i:j] in word_set:
                # If a word matches, recurse from the end of the word
                min_extra = min(min_extra, helper(j))
        
        mem[i] = min_extra  # Store the result in the memo table
        return mem[i]
    return helper(0)

print(minExtraChar("metzeaencgpgvsckjrqafkxgyzbe", ["zdzz","lgrhy","r","ohk","zkowk","g","zqpn","anoni","ka","qafkx","t","jr","xdye","mppc","bqqb","encgp","yf","vl","ctsxk","gn","cujh","ce","rwrpq","tze","zxhg","yzbe","c","o","hnk","gv","uzbc","xn","kk","ujjd","vv","mxhmv","ugn","at","kumr","ensv","x","uy","gb","ae","jljuo","xqkgj"]))