def maxUniqueSplit(s: str) -> int:
    found = set([])
    count = 0
    def helper(s: str, m: set):
        if not s:
            return len(m)
        counts = []
        for i in range(len(s)):
            if s[:i+1] not in m:
                k = m.copy()
                k.add(s[:i+1])
                counts.append(helper(s[i+1:], k))
        if counts: return max(counts)
        else: return len(m)
    return helper(s, found)

print(maxUniqueSplit("wwwzfvedwfvhsww"))