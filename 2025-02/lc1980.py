from typing import List

def findDifferentBinaryString(nums: List[str]) -> str:
    n = len(nums[0])
    nums = set(nums)
    
    for i in range(2^16):
        b = bin(i)[:1:-1].zfill(n)
        if b not in nums:
            return b

print(findDifferentBinaryString(["0000000011","0000000111","0000000110","0000001000","0000000000","0000000010","0000000101","0000000001","0000000100","1111111111"]))