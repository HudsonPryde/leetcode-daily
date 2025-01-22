def twoSum(nums, target):
    d = {}
    for i in range(0, len(nums)):
        diff = target - nums[i]
        if diff in d:
            return [i, d[diff]]
        else:
            d[nums[i]] = i

print(twoSum([2,7,-11,15], -4))
