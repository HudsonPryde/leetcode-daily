def findCompliment(num: int) -> int:
    return num^((1<<num.bit_length())-1)
print(findCompliment(50))