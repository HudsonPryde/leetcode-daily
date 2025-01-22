from typing import List


def maximumBeauty(nums: List[int], k: int) -> int:
    n = len(nums)
    nums.sort(reverse=True)
    low = nums[0]-k
    p = 0
    max_len = 0
    for i in range(n):
        # increase max len as long as the curr range high val is over the stored low val
        if nums[i]+k < low:
            max_len = max(i-p, max_len)
            # find earliest val in range
            while p < n and nums[p]-k > nums[i]+k:
                p += 1
            low = nums[p]-k
    return max(n-p, max_len)
print(maximumBeauty([1,1,1,1],10))