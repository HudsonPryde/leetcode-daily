class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minCount = blocks.count("W")
        for i in range(len(blocks)-k+1):
            minCount = min(minCount, blocks[i:i+k].count("W"))
        return minCount
s = Solution()
print(s.minimumRecolors("WWBBBWBBBBBWWBWWWB",16))