class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        n = max(len(version1),len(version2))
        for i in range(n):
            a,b = 0,0
            if i < len(version1):
                a = int(version1[i])
            if i < len(version2):
                b = int(version2[i])
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0

print(Solution().compareVersion("1.2","1.10"))