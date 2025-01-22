def canBeValid(s: str, locked: str) -> bool:
    if len(s)%2==1: return False
    if s == "()": return True
    if locked[0] == 1 and s[0] == ")": return False
    if locked[-1] == 1 and s[-1] == "(": return False

    stack = []
    lock = []
    for i in range(len(s)):
        p, mode = s[i], locked[i]
        if mode=="1" and p==")":
            if stack: 
                if lock:
                    prev = lock.pop()
                    stack.pop(prev)
                else: stack.pop()
            else: return False
            continue
        elif mode=="1" and p=="(":
            lock.append(len(stack))
        stack.append((p,mode))
    
    unlocked = 0
    while stack:
        p,mode = stack.pop()
        if mode == "0":
            unlocked += 1
        else:
            unlocked -= 1
            if unlocked < 0:
                return False
    
    return True

print(canBeValid("())()))()(()(((())(()()))))((((()())(())", "1011101100010001001011000000110010100101"))