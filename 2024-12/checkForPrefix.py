def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    for i,word in enumerate(sentence.split()):
        if len(word) >= len(searchWord):
            if word.startswith(searchWord): return i 
    return -1