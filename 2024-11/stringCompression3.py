def compressedString(word: str) -> str:
    res = ''
    cnt = 0
    prev = None
    for c in word:
        if prev == None:
            prev = c
            cnt = 1
        elif c != prev or cnt == 9:
            res += str(cnt) + prev
            cnt = 1
            prev = c
        else:
            cnt += 1
    res += str(cnt)+prev
    return res

print(compressedString("abcde"))