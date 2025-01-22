def repeatLimitedString(s: str, repeatLimit: int) -> str:
    d = {}
    res = ""
    for l in s:
        d[l] = d.get(l,0)+1
    k = sorted(d.keys())
    while k:
        c = k.pop()
        res += c*min(repeatLimit,d[c])
        d[c] -= min(repeatLimit,d[c])
        if d[c] > 0:
            if not k: break
            p = k.pop()
            res += p
            d[p] -= 1
            if d[p] > 0:
                k.append(p)
            k.append(c)
    return res
print(repeatLimitedString("xyutfpopdynbadwtvmxiemmusevduloxwvpkjioizvanetecnuqbqqdtrwrkgt", 1))
# expected: zyxyxwxwvwvuvuvututstrtrtqpqpqponononmlmkmkjigifiededededcbaba