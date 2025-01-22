def minLength(s: str) -> int:
    def helper(s: str):
        if len(s) == 0:
            return s
        new_s = s.replace("AB", "").replace("CD", "")
        if new_s == s:
            return s
        return helper(new_s)
    return len(helper(s))

def minLengthV2(s: str) -> int:
    t = []
    idx = 0
    while idx < len(s):
        if not t:
            t.append(s[idx])
            idx += 1
            continue
        if (t[-1] == "A" and s[idx] == "B") or (t[-1] == "C" and s[idx] == "D"):
            t.pop()
        else:
            t.append(s[idx])
        idx += 1
    return len(t)


print(minLengthV2("ABFCACDB"))
