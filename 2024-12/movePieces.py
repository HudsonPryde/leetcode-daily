def canChange(start: str, target: str) -> bool:
    n = len(start)
    # track the indices of the nodes in the list
    p1, p2 = [], []
    for i in range(n):
        if start[i] != "_":
            p1.append(start[i])
        if target[i] != "_":
            p2.append(target[i])
    
    if len(p1) != len(p2): return False

    for i in range(len(p1)):
        if start[p1[i]] != target[p2[i]]: return False
        if start[p1[i]] == "L" and p2[i] > p1[i]: return False
        if start[p1[i]] == "R" and p2[i] < p1[i]: return False
    return True