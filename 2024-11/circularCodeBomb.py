from typing import List


def decrypt(code: List[int], k: int) -> List[int]:
    n = len(code)
    pre_sum1 = [code[0]]
    pre_sum2 = [0]*n
    pre_sum2[-1] = code[-1]
    for i in range(1, n):
        pre_sum1.append(pre_sum1[i-1] + code[i])
    for i in range(n-2, -1, -1):
        pre_sum2[i] = pre_sum2[i+1] + code[i]
    res = []
    print(pre_sum1)
    print(pre_sum2)
    for i in range(n):
        t = 0
        if k > 0:
            if i == n-1: t += pre_sum1[i-1]
            else:
                d = i+abs(k)
                t -= pre_sum1[i]
                # if d > n-1 go into sum arr 2
                if d >= n: t += pre_sum2[-d+(d-n)]
                if d < n: t += pre_sum1[d]
            res.append(t)
        else:
            # if at 0 just add sum arr 2 at k
            if i == 0: t += pre_sum2[k]
            else:
                # find idx travelled to in arr 1
                d = i-abs(k)
                t += pre_sum1[i-1]
                # if less than 0 add the diff from sum arr 2
                if d < 0: 
                    t += pre_sum2[d]
                elif d > 0:
                    t -= pre_sum1[d-1]
            res.append(t)
    return res


    
print(decrypt([5,7,1,4],3))