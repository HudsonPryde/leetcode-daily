def fractionAddition(expression: str) -> str:
    exp = expression.replace("-", "+-")
    exp = exp.split("+")
    if exp[0] == "":
        exp.pop(0)
    total = [0,1]
    for i in range(len(exp)):
        n, d = exp[i].split("/")
        n,d = int(n),int(d)
        if total[1] != d:
            n *= total[1]
            total[1] *= d
            total[0] *= d
            
        total[0] += n
    if total[0] == 0:
        return "0/1"
    a,b = total[0], total[1]
    while b:
        a,b = b, a%b
    return str(total[0]//a)+"/"+str(total[1]//a)


print(fractionAddition("-1/3+1/4-1/5+1/6-1/7+1/8-1/9+1/10-1/9+1/10"))

