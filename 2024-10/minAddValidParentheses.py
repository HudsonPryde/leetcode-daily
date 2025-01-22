def minAddToMakeValid(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    def helper(s: str):
        if len(s) == 0:
            return 0
        new_s = s.replace('()', '')
        if len(new_s) == len(s):
            return len(s)
        return helper(new_s)
    return helper(s)

print(minAddToMakeValid("()))"))