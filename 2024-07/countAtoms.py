def countOfAtoms(formula: str) -> str:
    stack = []
    formula = list(formula)
    while formula:
        l = formula.pop(0)
        if stack and l.isnumeric() and stack[-1] == ")":
            mult = [l]
            while formula and formula[0].isnumeric():
                mult.append(formula.pop(0))
            mult = int("".join(mult))
            atom = []
            num = []
            s = []
            k = stack.pop()
            while k != "(":
                if k.isnumeric():
                    num.append(k)
                elif k.isalpha():
                    if k.isupper():
                        atom.append(k)
                        s.extend(reversed(atom))
                        if num:
                            s.extend(str(int("".join(reversed(num))) * mult))
                        else:
                            s.extend(str(mult))
                        atom.clear()
                        num.clear()
                    else:
                        atom.append(k)
                k = stack.pop()
            stack.extend(s)
        else:
            stack.append(l)

    count = {}
    atom = []
    num = []
    for i, l in enumerate(stack):
        if l.isalpha():
            if atom and l.isupper():
                a, n = "".join(atom), "".join(num)
                if num:
                    count[a] = count.get(a, 0) + int(n)
                else:
                    count[a] = count.get(a, 1)
                atom.clear()
                num.clear()
            atom.append(l)
        elif l.isnumeric():
            num.append(l)
        if i == len(stack) - 1:
            a, n = "".join(atom), "".join(num)
            if num:
                count[a] = count.get(a, 0) + int(n)
            else:
                count[a] = count.get(a, 1)

    con = []
    for a, n in count.items():
        if n > 1:
            con.append(a + str(n))
        else:
            con.append(a)
    return "".join(sorted(con))
      
    
  
print(countOfAtoms("(((K4(ON(SO3)2)3(Fe(CN)6)2)4(Mg(OH)2)10)2(H2O)5)3"), " expected: C288Fe48H150K96Mg60N360O639S144")
