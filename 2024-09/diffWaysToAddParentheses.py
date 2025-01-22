from typing import List
import itertools

def diffWaysToCompute(expression: str) -> List[int]:
    res = []
    # ans = []
    for i in range(len(expression)):
        oper = expression[i]
        if oper == "+" or oper == "-" or oper == "*":
            sub_str1 = expression[0 : i]
            sub_str2 = expression[i + 1 : ]
            s1 = diffWaysToCompute(sub_str1)
            s2 = diffWaysToCompute(sub_str2)
            for i in s1:
                for j in s2:
                    if oper == "*":
                        res.append(int(i) * int(j))
                    if oper == "+":
                        res.append(int(i) + int(j))
                    if oper == "-":
                        res.append(int(i) - int(j))
    if len(res) == 0:
        res.append(int(expression))
    # print(res)
    return res

print(diffWaysToCompute("2-1-1"))
        