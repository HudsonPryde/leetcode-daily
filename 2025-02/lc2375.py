def smallestNumber(pattern: str) -> str:
    def helper(s: list, nums: list, pat: str):
        if pat == '':
            return s
        for i in range(len(nums)):
            if (pat[0] == "I" and nums[i] > s[-1]) or (pat[0] == "D" and nums[i] < s[-1]):
                res = helper(s+[nums[i]], nums[:i]+nums[i+1:], pat[1:])
                if res:
                    return res
    for i in range(1, 10):
        res = helper([i],[n for n in range(1, 10) if n != i], pattern)
        if res:
            return ''.join([str(r) for r in res])

print(smallestNumber("DDD"))
                

