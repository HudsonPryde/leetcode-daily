from typing import List


def longestPalindrome(words: List[str]) -> int:
    m = {}
    p = {}
    for w in words:
        if w[::-1] != w:
            m[w] = m.get(w,0)+1
        else:
            p[w] = p.get(w,0)+1
    l = 0
    
    for w in m.keys():
        if w[::-1] in m:
            l += min(m[w], m[w[::-1]])*2
    
    total = 0
    has_odd = 0
    for n in p.values():
        if n%2 == 0:
            total += n*2
        else:
            total += (n-1)*2
            has_odd = 2
    return l+total+has_odd

print(longestPalindrome(["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]))