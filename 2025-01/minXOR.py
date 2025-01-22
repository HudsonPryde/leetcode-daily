def minimizeXor(num1: int, num2: int) -> int:
    dif = num2.bit_count() - num1.bit_count()
    if dif > 0:
        for _ in range(dif):
            num1 = num1|(num1+1)
        return num1
    else:
        for _ in range(dif*-1):
            num1 = num1&(num1-1)
        return num1

print(minimizeXor(1000000000,255))
