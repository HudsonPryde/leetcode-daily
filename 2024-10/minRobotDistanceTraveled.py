from typing import List


def minimumTotalDistance(robot: List[int], factory: List[List[int]]) -> int:
    factory.sort(key=lambda x: x[0])
    robot.sort()

    f_pos = []
    for f in factory:
        for _ in range(f[1]):
            f_pos.append(f[0])
    
    r_count, f_count = len(robot), len(f_pos)
    dp = [[0]*(f_count+1) for _ in range(r_count+1)]

    for i in range(r_count):
        dp[i][f_count] = 1e12

    for i in range(r_count-1, -1, -1):
        for j in range(f_count-1, -1, -1):
            assign = abs(robot[i] - f_pos[j]) + dp[i+1][j+1]
            skip = dp[i][j+1]
            dp[i][j] = min(assign,skip)

    return dp[0][0]

print(minimumTotalDistance([1,-1], [[-2,1],[2,1]]))