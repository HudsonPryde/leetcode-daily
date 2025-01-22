def shortestPalindrome(s: str) -> str:
    if len(s) <= 1:
        return s
    for i in range(len(s)-1, 0, -1):
        if s[:i] == s[i-1::-1]:
            return s[:i-1:-1]+s
def KMP(s: str) -> str:
    if len(s) <= 1:
        return s
    s2 = s+"#"+s[::-1]
    l, r = 0, 1
    t = [None]*len(s2)
    while r < len(s2):
        if s2[l] == s2[r]:
            t[r] = l
            l,r = l+1, r+1
        elif l and t[l-1] is not None:
            l = t[l-1] + 1
        elif l:
            l = 0
        else:
            r += 1
    return s[::-1][:len(s)-t[-1]-1] + s



print(KMP("aacecaaa"))