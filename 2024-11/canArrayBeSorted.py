from typing import List


def canSortArray(nums: List[int]) -> bool:
    for i in range(1, len(nums)):
        a, b = nums[i-1], nums[i]
        idx = i
        while a > b and idx > 0:
            a_bin, b_bin = bin(a).count("1"), bin(b).count("1")
            if a_bin != b_bin:
                return False
            else:
                nums[idx], nums[idx-1] = a, b
            idx -= 1
            a, b = nums[idx-1], nums[idx]
    return True

print(canSortArray([177,29,256]))