from bisect import bisect_left
from typing import List
valid = [True] * 1001
valid[0] = valid[1] = False
for i in range(2, len(valid)):
    if valid[i]:
        for j in range(i * i, len(valid), i):
            valid[j] = False
primes = [i for i in range(len(valid)) if valid[i]]

def primeSubOperation(nums: List[int]) -> bool:
    prev = 0
    for num in nums:
        if num <= prev:
            return False
        i = bisect_left(primes, num-prev)-1
        if i != -1:
            num -= primes[i]
        prev = num



print(primeSubOperation([4,9,6,10]))