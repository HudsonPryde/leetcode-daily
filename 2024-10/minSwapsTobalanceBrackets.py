
def minSwaps(s: str) -> int:
    st = 0
    for b in s:
        if b == "[":
            st += 1
        else:
            if st > 0:
                st -= 1
    return (st+1) // 2

print(minSwaps("]][[[]]][[]][][["))