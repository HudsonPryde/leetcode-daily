def isCircularSentence(sentence: str) -> bool:
    sentence = sentence.split(" ")
    if sentence[0][0] != sentence[-1][-1]:
        return False
    prev = None
    for w in sentence:
        if prev and prev != w[0]:
            return False
        prev = w[-1]
    return True
        
print(isCircularSentence("leetcode exercises sound delightful"))