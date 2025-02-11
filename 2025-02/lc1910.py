def removeOccurrences(s: str, part: str) -> str:
    while part in s:
        s = s.replace(part, '', 1)
    return s

print(removeOccurrences("aabababa", "aba"))