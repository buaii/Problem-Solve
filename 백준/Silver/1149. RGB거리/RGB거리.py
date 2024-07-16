import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline
import itertools

n = int(input().strip())

data = [list(map(int, input().strip().split())) for _ in range(n)]
# N이 2이상이므로 dp[0] 설정 가능
dp = [[data[0][0], data[0][1], data[0][2]] for _ in range(n)]


for i in range(1, n):
    # R을 선택할 때 이전 단계의 G,B 중 최솟값 선택
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + data[i][0]
    # G를 선택할 때 이전 단계의 R,B 중 최솟값 선택
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + data[i][1]
    # B를 선택할 때 이전 단계의 R,G 중 최솟값 선택
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + data[i][2]
sys.stdout.write(f"{min(dp[n-1])}")