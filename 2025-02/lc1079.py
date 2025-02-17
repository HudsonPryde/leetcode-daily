from itertools import permutations
def numTilePossibilities(tiles: str) -> int:
    res = set()
    for i in range(1,len(tiles)+1):
        res.update(permutations(tiles, i))
    return len(res)

print(numTilePossibilities("AAABBC"))