from collections import Counter
from typing import List


def canReorderDoubled(arr: List[int]) -> bool:
    c = Counter(arr)
    arr = list(set(arr))
    arr.sort(key=lambda x: abs(x))
    n = len(arr)
    for i in range(n):
        if c[arr[i]] == 0:
            continue
        if 2*arr[i] in c:
            if arr[i] == 0 and c[arr[i]]%2 == 1:
                return False
            elif c[arr[i]] <= c[2*arr[i]]:
                c[2*arr[i]] -= c[arr[i]]
                c[arr[i]] = 0
                continue
        return False
    return True

# print(canReorderDoubled([1,2,1,-8,8,-4,4,-4,2,-2]))
def authEvents(events):
    # Write your code here
    curr_pass = 0
    result = []
    for command, value in events:
        if command == "setPassword":
            curr_pass = 0
            n = len(value)
            for i in range(n):
                curr_pass += (ord(value[i])*(131**(n-1-i)))
            curr_pass = curr_pass%((10**9)+7)
            print(curr_pass)
        elif command == "authorize":
            x = int(value)
            
            # Check if the provided x is the hash of the current password
            if x == curr_pass:
                result.append(1)
            else:
                # Check if x is the hash of the current password with one character appended
                found_match = False
                for c in range(48, 123):  # ASCII range for digits, uppercase, and lowercase letters
                    new_hash = (curr_pass * 131 + c) % ((10**9)+7)
                    if new_hash == x:
                        found_match = True
                        result.append(1)
                        break
                if not found_match:
                    result.append(0)
    return result

authEvents([["setPassword", "zzzzzzzza"]])
print((10**9)+7)
print(((10**9)+7)//900)

# max: 10 k: 1
# [0,0,0,0,0]
# [0,1,0,0,0]
# [1,2,1,0,0]
# [2,3,2,1,0]
# [3,4,2,1,0]