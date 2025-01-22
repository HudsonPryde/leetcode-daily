def areSentencesSimilar(sentence1: str, sentence2: str) -> bool:
    if len(sentence1) > len(sentence2):
        s1 = sentence2.split()
        s2 = sentence1.split()
    elif len(sentence1) == len(sentence2):
        return sentence1 == sentence2
    else:
        s2 = sentence2.split()
        s1 = sentence1.split()
    n1,n2 = len(s1),len(s2)
    g1,g2 = s2[:n1], s2[n2-n1:]
    if g1 == s1 or g2 == s1: return True
    for i in range(len(s1)):
        k1,k2 = s2[:i], s2[n2-n1+i:]
        h1,h2 = s1[:i], s1[i:]
        if k1 == h1 and k2 == h2: return True
    
    return False

print(areSentencesSimilar("hello racecar", "hello racecar acecar"))