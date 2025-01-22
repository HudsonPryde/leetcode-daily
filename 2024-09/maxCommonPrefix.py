from typing import List


def longestCommonPrefix(arr1: List[int], arr2: List[int]) -> int:
    arr1, arr2 = list(set(arr1)), list(set(arr2))
    res = 0
    pre1 = {}
    def helper(n, d):
        if len(n) == 0:
            return d
        if n[0] not in d:
            d[n[0]] = {}
        return helper(n[1:], d[n[0]])
    for n in arr1:
        helper(str(n), pre1)
    arr2.sort(reverse=True)
    def solve(n, d, l):
        if len(n) == 0:
            return l
        if n[0] not in d:
            return l
        return solve(n[1:], d[n[0]], l+1)
    for n in arr2:
        s = str(n)
        if len(s) < res:
            continue
        res = max(res, solve(s, pre1, 0))
    return res

print(longestCommonPrefix([1,10,100], [1000]))