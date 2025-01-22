import math
def maximumSwap(num: int) -> int:
    num = list(str(num))
    
    for i in range(len(num)):
        if int(num[i]) < 9:
            max_n = int(num[i])
            n_i = None
            for k in range(len(num)-1, i, -1):
                if int(num[k]) > max_n:
                    max_n = int(num[k])
                    n_i = k
            if n_i:
                num[i],num[n_i] = str(max_n),num[i]
                break

    return "".join(num)

# print(maximumSwap("98368"))
n = [3,4,1,2]
print(sorted(n)[math.floor(len(n)/2)-1])