from collections import defaultdict

def countPalindromicSubsequence(s: str) -> int:
    n = len(s)
    left_seen = defaultdict(str)
    right_seen = defaultdict(str)
    # get left most indices of letters
    for i in range(n):
        if s[i] not in left_seen:
            left_seen[s[i]] = i
    for j in range(n-1,-1,-1):
        if s[j] not in right_seen:
            right_seen[s[j]] = j
    res = 0
    # add up unique keys between left and right values
    for k,v in left_seen.items():
        if right_seen[k] == v: continue
        res += len(set(s[v+1:right_seen[k]]))

    return res
print(countPalindromicSubsequence("bbcbaba"))