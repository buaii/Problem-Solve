import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    data = [list(map(int, input().strip().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]
    
    # 1열
    dp[0][0] = data[0][0]
    dp[1][0] = data[1][0]
    # 2열
    if n > 1:
        dp[0][1] = data[1][0] + data[0][1]
        dp[1][1] = data[0][0] + data[1][1]
    # n이 3이상
    for i in range(2, n):
        # max(1열만 선택하고 2열은 패스하는 경우 / 1,2열 둘 다 선택 )             
        dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + data[0][i]
        dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + data[1][i]
    sys.stdout.write(f"{max(dp[0][n-1], dp[1][n-1])}\n")
