def parseBoolExpr(expression: str) -> bool:
    n = len(expression)
    ops = []
    res = None
    bools = set()
    
    for i in range(n):
        if expression[i] in ["!","|","&","t","f"]:
            ops.append(expression[i])
        elif expression[i] == ")":
            curr_bools = set()
            while ops:
                op = ops.pop()
                if op in ['t','f']:
                    curr_bools.add(op)
                else:
                    if op == "!":
                        if len(curr_bools) == 2:
                            ops.extend(['t','f'])
                        elif 't' in curr_bools:
                            ops.append('f')
                        else:
                            ops.append('t')
                    elif op == "|":
                        if 't' in curr_bools: ops.append('t')
                        else: ops.append('f')
                    else:
                        if 'f' not in curr_bools: ops.append('t')
                        else: ops.append('f')
                    break
    if ops[0] == 't': return True
    else: return False

print(parseBoolExpr("!(&(!(t),&(f),|(f)))"))