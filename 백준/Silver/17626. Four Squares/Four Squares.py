import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())

dp = [0, 1]


for i in range(2, n+1):
	minimum = 4
	for j in range(1, int(i**0.5) + 1):
			minimum = min(minimum, dp[i - j**2])
	dp.append(minimum+1)
sys.stdout.write(f"{dp[n]}")